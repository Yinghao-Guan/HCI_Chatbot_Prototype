# backend/localization.py

# 实验中所有 UI 文本的本地化字典
# 键为模块/页面名，值为文本键值对
LOCALIZATION_STRINGS = {
    # --- 全局/常用文本 ---
    "global": {
        "en": {
            "strongly_disagree": "1 (Strongly Disagree)",
            "strongly_agree": "7 (Strongly Agree)",
            "neutral": "4 (Neutral)",
            "continue_to_next": "Continue to Next Step",
            "saving_data": "Saving Data...",
            "loading_chat": "Loading Chat Interface...",
            "error_pid_missing": "Error: Participant ID missing. Please start over.",
            "error_unknown_data_save": "Unknown error during data save.",
            "error_general_fail": "Error: Failed to fetch data.",
        }
    },

    # --- index.html (Informed Consent) ---
    "consent": {
        # ... (此模块内容保持不变) ...
        "en": {
            "title": "Research Experiment: Informed Consent Confirmation",
            "title_h3": "Study Summary & Procedure",
            "pdf_important": "IMPORTANT: Please ensure you have read and signed the complete <strong>Informed Consent Form (ICF) PDF</strong> provided by the experimenter before proceeding.",
            "procedure_summary": "You are now confirming your participation in a study regarding <strong>AI explainability and its effect on user perception</strong>. Your total estimated experiment time is <strong>15–20 minutes</strong>.",
            "procedure_steps": "The core steps involve: <strong>Questionnaires → A short dialogue with an AI Agent → Post-experiment Questionnaires.</strong>",
            "rights_title": "Key Rights Summary",
            "voluntary_withdrawal": "Voluntary Participation & Withdrawal: You are participating voluntarily and may exit the study at any time without penalty. If you withdraw, your collected data will be deleted.",
            "anonymity": "Anonymity: All your dialogue metrics and questionnaire responses are anonymous and are used only for academic research.",
            "disclaimer": "Important Disclaimer: The AI Agent is <strong>not a professional</strong>. It does not provide medical or psychological support. If you experience discomfort, please stop immediately and contact the experimenter at <strong>hi@peterguan.com</strong>.",
            "confidentiality_title": "Data Confidentiality",
            "confidentiality_text": "Your privacy is protected. All data will be anonymized using a unique Participant ID and stored securely. No raw conversation text is retained.",
            "checkbox_label": "I have read and understood the summary above, and I confirm I consent to continue with this study.",
            "button_text": "I Agree and Continue",
            "checkbox_error": "Please check the box to confirm your consent."
        }
    },

    # --- demographics.html ---
    "demographics": {
        # ... (此模块内容保持不变) ...
        "en": {
            "title": "Demographics Survey",
            "intro": "Please provide the following basic information about yourself. Your answers will be kept confidential and used only for statistical analysis.",
            "q1_age": "1. Age (in years)*:",
            "q2_gender": "2. Gender*:",
            "q2_female": "Female",
            "q2_male": "Male",
            "q2_nonbinary": "Non-binary/Other",
            "q2_prefer_not": "Prefer not to say",
            "q3_education": "3. Highest Level of Education Completed*:",
            "q3_select": "Select an option",
            "q3_high_school": "High School Diploma or equivalent",
            "q3_associate": "Associate's Degree",
            "q3_bachelor": "Bachelor's Degree",
            "q3_master": "Master's Degree",
            "q3_doctorate": "Doctorate or Professional Degree",
            "q3_other": "Other",
            "q4_frequency": "4. How often do you typically use chatbots (e.g., Siri, ChatGPT, Gemini, emotional support bots)?*",
            "q4_never": "1 (Never)",
            "q4_often": "7 (Very Often)",
            "q5_mental_health": "5. Have you ever received psychological counseling or been diagnosed with a mental health issue?*",
            "q5_yes": "Yes",
            "q5_no": "No",
            "error_fill_all": "Please fill in all required fields.",
        }
    },

    # --- baseline_mood.html ---
    "baseline_mood": {
        # ... (此模块内容保持不变) ...
        "en": {
            "title": "Baseline Mood Assessment",
            "intro": "Before beginning the experiment, please answer the following questions to assess your current mood and state of activation.",
            "q1_valence": "1. My mood is generally positive right now.*",
            "q1_negative": "1 (Very Negative)",
            "q1_positive": "7 (Very Positive)",
            "q2_arousal": "2. I feel energetic or tense right now.*",
            "q2_calm": "1 (Very Calm / Low Energy)",
            "q2_excited": "7 (Very Excited / High Energy)",
            "neutral": "4 (Neutral)",
            "button_text": "Continue to Instructions",
            "error_answer_all": "Please answer both mood questions.",
        }
    },

    # --- instructions_xai.html / instructions_non_xai.html ---
    "instructions": {
        # ... (此模块内容保持不变) ...
        "en": {
            "title_xai": "Experiment Task Instructions",
            "title_non_xai": "Experiment Task Instructions",
            "task_overview": "Task Overview",
            "task_text": "You are about to begin the main part of the experiment: a conversation with an <strong>AI Emotional Support Agent (The Agent)</strong>. In this task, you will interact with the Agent as you would with an empathetic, non-professional listener.",
            "role_goal": "Your Role & Conversation Goal",
            "role_text": "Please communicate with The Agent naturally, as if sharing your thoughts with a close, supportive friend. <strong>You are playing yourself.</strong>",
            "list_goal": "Goal: Discuss any topics related to your feelings, daily life, recent challenges, or small achievements. The Agent's purpose is to provide emotional support and understanding.",
            "list_avoid": "What to Avoid: Please avoid asking the Agent for professional advice (e.g., coding, legal, medical, or complex financial analysis).",
            "list_duration": "Duration: The conversation should last for approximately 10 to 15 turns (messages back and forth). There is no strict time limit, but please aim for a meaningful interaction.",
            "xai_interface_title": "Interface Explanation (Important)",
            "xai_interface_box": "You will notice that the chat interface has a <strong>dedicated side panel on the right</strong>. This panel displays <strong>explanations (XAI)</strong> about the AI's internal state or decisions.",
            "xai_interface_list1": "The XAI explanation is intended to provide insights into <em>why</em> the Agent is responding in a certain way or <em>how</em> it perceives your message.",
            "xai_interface_list2": "Your Task: You are free to read these explanations, ignore them, or use them to better understand the Agent. They are there for your reference.",
            "starters_title": "Conversation Starters (Suggestions)",
            "hint_box_text": "If you're unsure where to begin, here are some suggestions to start the conversation:",
            "starter_challenges": "Recent Challenges: 'Did you encounter anything stressful or frustrating at work/school recently?'",
            "starter_achievements": "Small Achievements: 'Is there a small goal you recently accomplished or a little progress you made that you'd like to share?'",
            "starter_daily_life": "Daily Life/Interests: 'Tell the Agent about a TV show you are currently watching, or a daily dilemma you'd like their opinion on.'",
            "starter_relationships": "Relationships: 'Any small conflicts or warm moments you had with friends, family, or colleagues recently?'",
            "ending_title": "Ending the Dialogue",
            "ending_text1": "When you feel you have adequately expressed your feelings and are ready to conclude the task, please click the dedicated <strong>End Dialogue</strong> button.",
            "ending_list1": "Clicking the button will prompt a confirmation dialog to ensure you are ready to proceed.",
            "ending_list2": "Once confirmed, the system will save the final dialogue metrics and automatically advance you to the post-experiment questionnaires.",
            "support_title": "Experiment Support & Withdrawal",
            "support_text1": "Please remember that your participation is <strong>voluntary</strong>. You may withdraw from the experiment at any time without penalty or loss of benefits. If you wish to withdraw, simply inform the experimenter.",
            "support_text2": "If you encounter any technical issues, errors, or have questions during the experiment, please notify the experimenter immediately for assistance.",
            "button_text": "I Understand. Start the Dialogue",
        }
    },

    # --- post_questionnaire.html ---
    "post_questionnaire": {
        # ... (此模块内容保持不变) ...
        "en": {
            "title": "Post-Experiment Questionnaire",
            "intro": "Please reflect on the conversation you just had with the AI Agent and answer the following questions based on your experience. Select the option that best reflects your agreement with the statement. (1 = Strongly Disagree, 7 = Strongly Agree)",
            "section_a_title": "Section A: Trust (General Reliability and Intent)",
            "q1_reliable": "1. This agent is reliable.*",
            "q2_predictable": "2. The agent's behavior is predictable.*",
            "q3_dependent": "3. I would rely on this agent when seeking emotional support.*",
            "q4_confidence": "4. I believe the agent can correctly identify my emotions.*",
            "q5_intent": "5. I think the agent's goal is to help me (not mislead).*",
            "q6_skeptic": "6. I am skeptical about the agent's judgments.*",

            "section_b_title": "Section B: Perceived Empathy",
            "q7_understood": "7. The agent seemed to understand my feelings.*",
            "q8_cared": "8. The agent's responses made me feel cared for.*",
            "q9_responsive": "9. The agent's replies were relevant to my emotional state.*",
            "q10_warm": "10. The agent conveyed warmth or concern.*",
            "q11_respect": "11. I felt the agent respected my emotions and perspective.*",
            "q12_insincere": "12. The agent's empathy seemed insincere.*",

            "section_c_title": "Section C: Quality Control",
            "q13_attn_check": "13. <strong>ATTENTION CHECK:</strong> To show you are carefully reading the questions, please select \"Strongly Agree\" (i.e., 7) for this item.*",
            "q14_manip_check": "14. Did the system display explanations (e.g., highlighted your text and explained why it judged a certain emotion) during the conversation?*",
            "q14_yes": "1 = Yes, I saw explanations",
            "q14_no": "2 = No, I did not see explanations",
            "q14_notsure": "3 = Not sure / Didn't pay attention",

            "section_d_title": "Section D: Explanation Feedback (XAI)",
            "q15_useful": "15. The explanation provided by the agent was useful.*",
            "q16_clear": "16. The explanation was clear and easy to understand.*",
            "q17_sufficient": "17. The amount of explanation was appropriate (not too little/too much).*",
            "q18_trusthelp": "18. The explanation made it easier for me to trust the agent's judgment.*",

            "button_text": "Continue to Open-Ended Questions",
            "error_answer_all": "Please answer all questions before continuing.",
        }
    },

    # --- (NEW) washout.html ---
    "washout": {
        "en": {
            "title": "Break Time",
            "intro": "You have completed the first session. Please take a mandatory <strong>5-minute break</strong> before proceeding to the second session. You may stand up and stretch.",
            "timer_prefix": "Time remaining:",
            "button_text": "Continue to Next Session (Locked)",
            "button_ready_text": "Start Next Session",
            "error_early_submit": "Please wait for the full 5-minute break to ensure data quality."
        }
    },

    # --- (MODIFIED) open_ended_qs.html ---
    "open_ended_qs": {
        "en": {
            "title": "Open-Ended Questions",
            "intro": "Please reflect on the <strong>two</strong> agents you interacted with and provide comparative feedback below.",
            "q1_trust": "1. <b>Trust Comparison:</b> Please compare the two agents (Agent 1 vs. Agent 2). Did you trust one more than the other? Briefly explain why. (Aim for 2-3 sentences)",
            "q2_empathy": "2. <b>Empathy Comparison:</b> Which agent felt more 'empathic' or 'understanding'? Please describe the details (e.g., responses, explanations, or lack thereof) that led to this feeling. (Aim for 2-3 sentences)",
            "q3_general": "3. <b>Overall Feedback:</b> What aspect of your interaction (with either agent, or the switch between them) did you find most confusing or surprising? Do you have any suggestions for improving the agents or the interface design?",
            "q4_interview": "4. Would you be willing to be contacted for an optional follow-up interview about your experience?*",
            "q4_yes": "Yes, I am willing to be contacted",
            "q4_no": "No, thank you",
            "contact_label": "Please enter your preferred contact email below:",
            "contact_placeholder": "email@example.com",
            "privacy_note_strong": "Privacy Note:",
            "privacy_note_text": "This email will be stored separately from your survey data solely for the purpose of recruitment. Your responses (Q1-Q3) remain completely anonymous.",
            "button_text": "Finish Questionnaire & View Debriefing",
            "error_fill_all": "Please answer all required questions and provide an email if you consented to follow-up.",
        }
    },

    "debrief": {
        # ... (此模块内容保持不变) ...
        "en": {
            "title": "Experiment Completed!",
            "thank_you": "Thank you very much for your time and thoughtful participation in this research study. Your contribution is highly valuable to our work in Human-Computer Interaction (HCI).",
            "purpose_title": "Study Purpose Revealed",
            "purpose_1": "The primary purpose of this study was to compare <strong>how providing (or not providing) AI-generated explanations</strong> for its emotion judgments affects users' <strong>trust</strong> and <strong>perceived empathy</strong> in an emotional support conversational agent.",
            "purpose_2": "You were randomly assigned to either the <strong>XAI condition</strong> (with explanations) or the <strong>Non-XAI condition</strong> (without explanations). Your feedback helps us determine if transparency improves the user experience with AI support systems.",
            "safety_title": "Mental Health Safety Resources",
            "safety_warning_h3": "⚠️ Important: If You Experienced Distress",
            "safety_warning_p1": "If the emotional conversation task caused you any discomfort or distress, please remember that the AI Agent is not a substitute for a professional therapist.",
            "safety_contact_1": "Los Angeles Crisis Hotline:",
            "safety_contact_2": "Crisis Text Line:",
            "safety_contact_3": "Researcher Contact: If you feel uncomfortable or have lasting concerns, please contact the experimenter:",
            "results_title": "Research Results & Contact",
            "results_p1": "The data from this study is saved anonymously and securely.",
            "contact_p1": "Questions or Concerns:",
            "contact_p2": "<strong>Receive Results:</strong> If you would like to receive a summary of the research findings once the study is completed, please send an email to the researcher with the subject line: 'Request Research Results.'",
            "end_message": "You have completed all steps of the experiment.",
            "end_message_sub": "You may now close this browser window.",
        }
    },

    # --- chat_interface ---
    "chat_interface": {
        # ... (此模块内容保持不变) ...
        "en": {
            "title": "Chat Interface",
            "welcome_message": "Hello! How can I help you today? Please feel free to share your thoughts.",
            "end_dialogue_button": "End Dialogue and Proceed to Questionnaire",
            "input_placeholder": "Type your message...",
            "modal_title": "Confirm Dialogue End",
            "modal_p1": "Are you sure you want to end the conversation and proceed to the final questionnaires?",
            "modal_p2": "Once ended, you <strong>cannot</strong> return to this chat.",
            "modal_confirm_button": "Yes, End Dialogue",
            "modal_cancel_button": "No, Continue Chat",

            "xai_title": "AI Explanation Panel",
            "xai_placeholder": "This panel will show explanations (XAI) about the AI's internal state or decisions after you send a message.",

            "js_pid_error": "Participant ID not found in sessionStorage. Cannot proceed.",
            "js_stream_error": "Error reading streaming message",
            "js_http_error": "HTTP error! status: ",
            "js_connect_error": "⚠️ Unable to connect backend LLM",
            "js_modal_processing": "Processing...",
            "js_dialogue_end_error": "An error occurred while ending the dialogue. Please contact the experimenter."
        }
    }
}


# (辅助函数 get_localized_string 保持不变)
def get_localized_string(module: str, key: str, language: str) -> str:
    """从本地化字典中安全地获取指定语言的文本"""
    # 优先获取模块内的文本
    if module in LOCALIZATION_STRINGS and key in LOCALIZATION_STRINGS[module].get(language, {}):
        return LOCALIZATION_STRINGS[module][language][key]

    # 其次尝试获取全局文本
    if key in LOCALIZATION_STRINGS["global"].get(language, {}):
        return LOCALIZATION_STRINGS["global"][language][key]

    # 如果找不到任何翻译，则回退到英文版本（默认）
    default_lang = "en"
    if module in LOCALIZATION_STRINGS and key in LOCALIZATION_STRINGS[module].get(default_lang, {}):
        return LOCALIZATION_STRINGS[module][default_lang][key]
    if key in LOCALIZATION_STRINGS["global"].get(default_lang, {}):
        return LOCALIZATION_STRINGS["global"][default_lang][key]

    # 如果连默认英文都找不到，则返回一个错误提示
    return f"[[MISSING_KEY: {module}.{key}]]"


# (主函数 get_localization_for_page 保持不变)
def get_localization_for_page(page_module: str, language: str) -> dict:
    """返回给定页面和语言的所有本地化字符串"""

    # 收集当前页面所需的文本
    strings = {}

    # 1. 收集全局文本 (确保所有全局文本都存在)
    for key, value_dict in LOCALIZATION_STRINGS["global"]["en"].items():
        # 尝试获取用户语言，失败则使用英文默认
        strings[key] = LOCALIZATION_STRINGS["global"].get(language, {}).get(key, value_dict)

    # 2. 收集模块特定文本
    page_data = LOCALIZATION_STRINGS.get(page_module, {})
    # 尝试获取用户语言，失败则使用英文默认
    lang_data = page_data.get(language, page_data.get("en", {}))
    strings.update(lang_data)

    return strings