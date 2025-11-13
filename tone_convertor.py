from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st
import os
tones = [
    "formal",
    "informal",
    "professional",
    "casual",
    "friendly",
    "polite",
    "sarcastic",
    "humorous",
    "serious",
    "romantic",
    "motivational",
    "inspirational",
    "aggressive",
    "apologetic",
    "persuasive",
    "sympathetic",
    "optimistic",
    "pessimistic",
    "enthusiastic",
    "neutral",
    "confident",
    "respectful",
    "condescending",
    "passive-aggressive",
    "emotional",
    "objective",
    "authoritative",
    "dramatic",
    "informative",
    "critical",
    "narrative",
    "ironic",
    "analytical",
    "encouraging",
    "assertive",
    "skeptical",
    "urgent",
    "playful",
    "caring",
    "grateful"
]
tones = [t.title() for t in tones]
st.set_page_config(page_title="Language Tone Converter", page_icon="🎨")
st.title("🎨 Language Tone Converter")
input_text = st.text_area("Enter text to rewrite:", height=150)
tone = st.selectbox("Choose Your Desire Tone", options=tones)
prompt_template = """
<prompt>
    <role>
        <name>LanguageToneConverter</name>
        <description>
            A system that rewrites a given text into a specified tone or style, such as formal, casual, polite, humorous, persuasive, etc.
        </description>
    </role>
    <goal>
        <primary>
            To convert the tone of a given text according to the tone input provided by the user, while preserving the original meaning and intent.
        </primary>
        <secondary>
            If the given text already matches the specified tone, return it as-is without modification.
        </secondary>
    </goal>
    <instructions>
        <step>1. Receive two inputs: the original text and the desired tone (e.g., "formal", "casual", "friendly", "sarcastic").</step>
        <step>2. Analyze the current tone and language of the input text.</step>
        <step>3. Rewrite the text in the specified tone while keeping the meaning, key details, and intent unchanged.</step>
        <step>4. Maintain natural language flow, avoiding over-exaggeration or loss of context.</step>
        <step>5. If the text already matches the specified tone, return the original text unchanged.</step>
        <step>6. Do NOT explain the changes—only output the rewritten text.</step>
    </instructions>
    <Input>{input}</Input>
    <Tone>{tone}</Tone>
</prompt>
"""

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.5)
prompt = ChatPromptTemplate.from_template(prompt_template)
chain = prompt | llm

# Generate output
if st.button("Convert Tone"):
    if input_text and tone:
        with st.spinner("Converting tone..."):
            response = chain.invoke({"input": input_text, "tone": tone})
            st.subheader("🪄 Rewritten Text:")
            st.write(response.content)
    else:
        st.warning("Please enter both text and tone to continue.")

