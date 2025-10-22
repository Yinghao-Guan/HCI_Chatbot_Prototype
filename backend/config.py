import os

# --- 全局常量 ---

# Ollama API 配置
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5:1.5b"

# LLM 服务的系统提示
SYSTEM_PROMPT = (
    "You are a gentle and empathetic conversational partner. "
    "Always respond in a natural, human-like manner. "
    "Keep your responses consistent with the user's language. "
    "Do not comment on the user's language skills."
)

# 摘要生成间隔 (每进行 X 轮用户-AI对话后生成一次摘要)
SUMMARY_INTERVAL = 5

# 实验数据存储路径
# 我们会在应用启动时确保这个目录存在
DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")

# 实验版本配置 (用于手动指定)
VERSION_MAP = {
    "XAI": "/html/XAI_Version.html",
    "NON_XAI": "/html/non-XAI_version.html"
}

# 实验步骤序列 (用于流程控制)
EXPERIMENT_STEPS = [
    # 第一步：实验初始化 (由 index.html 触发，但实际不收集数据)
    "INIT",
    # 步骤 1: 人口统计信息
    "DEMOGRAPHICS",
    # 步骤 2: 基线情绪
    "BASELINE_MOOD",
    # 步骤 3: 任务说明 (此页面不收集数据)
    "INSTRUCTIONS",
    # 步骤 4: 对话实验
    "DIALOGUE",
    # 步骤 5: 实验后问卷
    "POST_QUESTIONNAIRE",
    # 步骤 6: 开放式问题
    "OPEN_ENDED_QS",
    # 步骤 7: 实验结束说明
    "DEBRIEF"
]