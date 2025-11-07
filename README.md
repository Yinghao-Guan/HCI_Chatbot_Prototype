# HCI Emotional Support Chatbot Prototype

## Overview

This is a full-stack web application built as a prototype for Human-Computer Interaction (HCI) research. It is designed to execute a formal experiment investigating the impact of **eXplainable AI (XAI)** on a user's **trust** and **perceived empathy** within an emotional support context.

This project implements a **within-subjects (or repeated measures), counterbalanced** experimental design, which is a more robust method than a simple A/B test. Each participant interacts with the chatbot under two distinct conditions:

1.  **XAI (Explainable) Condition**: The agent provides standard empathetic responses, accompanied by explanations in a side panel detailing *why* it is responding in a certain way or *how* it has interpreted the user's emotional state.

2.  **Non-XAI (Baseline) Condition**: The agent provides standard empathetic responses with no additional explanations.

Participants are assigned to a counterbalanced order (Group AB: XAI first, then Non-XAI; or Group BA: Non-XAI first, then XAI) to mitigate ordering effects. The entire experimental flow is managed by a Flask backend, ensuring data integrity and correct participant routing.

## Core Architecture: The Experimental Flow

The application is not a collection of static pages but a state-managed, linear experiment controlled by the backend. The experimenter's entry point is `html/admin_setup.html`.

The complete participant journey is as follows:

1.  **Admin Setup (`admin_setup.html`)**: The **experimenter** (not the participant) initiates the session by entering a `participant_id` and selecting the `condition_order` (AB or BA).

2.  **Informed Consent (`index.html`)**: The participant is redirected here. They review the study's purpose, their rights, and must consent to proceed.

3.  **Demographics (`demographics.html`)**: The participant provides basic background information.

4.  **Baseline Mood (`baseline_mood.html`)**: A pre-experiment questionnaire (using Likert scales) captures the participant's initial emotional state (valence and arousal).

5.  **Session 1 - Instructions**: The backend dynamically serves either `instructions_xai.html` or `instructions_non_xai.html` based on the participant's assigned (AB/BA) order.

6.  **Session 1 - Dialogue**: The participant is routed to the corresponding chat interface (`XAI_Version.html` or `non-XAI_version.html`).
    * The backend `llm_service.py` connects to a local **Ollama** instance (e.g., `qwen2.5:1.5b`) to generate streaming responses.
    * All dialogue interactions and metrics are logged by `data_manager.py`.

7.  **Session 1 - Post-Questionnaire (`post_questionnaire.html`)**:
    * The participant evaluates the agent they just interacted with on metrics of trust and empathy.
    * This page dynamically **hides or shows** the "Section D: Explanation Feedback" questions using JavaScript, based on the condition (XAI or Non-XAI) the participant just completed.

8.  **Washout Period (`washout.html`)**:
    * A **mandatory 5-minute break** with a timer.
    * This "washout" period is crucial in a within-subjects design to minimise carry-over effects from the first session to the second. The backend validates this duration.

9.  **Session 2 - Instructions**: The backend serves the instructions for the *other* condition (the one not yet experienced).

10. **Session 2 - Dialogue**: The participant is routed to the chat interface for the second condition.

11. **Session 2 - Post-Questionnaire (`post_questionnaire.html`)**: The participant evaluates the second agent.

12. **Comparative Questions (`open_ended_qs.html`)**:
    * This final questionnaire is presented only after *both* sessions are complete.
    * It explicitly asks the participant to **compare "Agent 1" and "Agent 2"** (e.g., "Trust Comparison", "Empathy Comparison"), gathering qualitative feedback on the differences they perceived.

13. **Debrief (`debrief.html`)**: The true purpose of the study (comparing XAI vs. Non-XAI) is revealed to the participant. Contact details and safety resources are provided.

## Key Features

* **Full-Stack Experiment Management**: A Flask backend manages participant state, data logging, and page routing.
* **Dynamic State Control**: The application tracks `current_step_index` for each participant, redirecting them to their correct page and preventing skipping or re-taking steps.
* **Within-Subjects Design**: Robustly supports a counterbalanced (AB/BA) repeated-measures study, a standard for rigorous HCI research.
* **LLM Integration**: Connects to a local Ollama instance (`llm_service.py`) for live, streaming chatbot responses.
* **Dynamic Questionnaires**: A single `post_questionnaire.html` file dynamically adapts its content based on the experimental condition, reducing code redundancy.
* **Comprehensive Data Logging**:
    * `P_{id}.jsonl`: A JSON Lines file logs all questionnaire data and turn-by-turn dialogue metrics (e.g., token count, char count) for each participant.
    * `follow_up_contacts.csv`: Optionally and separately stores contact details for participants who consent to a follow-up interview, preserving the anonymity of the primary data.
* **Localisation Support**: All user-facing text is managed centrally in `backend/localization.py` for easy translation and maintenance.

## Technology Stack

* **Backend**: Flask, requests
* **LLM**: Ollama (configured in `config.py` for `qwen2.5:1.5b`)
* **Frontend**: HTML5, CSS3, (Vanilla) JavaScript
* **Data Formats**: JSON Lines (.jsonl), JSON, CSV

## How to Run (Inferred)

1.  **Install Backend Dependencies**:

    ```bash
    pip install Flask flask_cors requests
    ```

2.  **Run Local LLM (Ollama)**:
    * Ensure the Ollama service is running locally.
    * Pull the required model: `ollama pull qwen2.5:1.5b`
    * Verify the `OLLAMA_API_URL` and `MODEL_NAME` in `backend/config.py` match your setup.

3.  **Start the Flask Server**:
    ```bash
    # From the project's root directory
    python backend/app.py
    ```
    The server will start on `http://127.0.0.1:5000`.

4.  **Begin the Experiment**:
    * The **experimenter** must navigate to the admin setup page in their browser:
        `http://127.0.0.1:5000/html/admin_setup.html`
    * Enter a unique Participant ID and select the Condition Order (AB or BA).
    * Clicking "Start" will initialise the participant's state file on the server and redirect the browser to the consent page (`index.html`), beginning the flow.
