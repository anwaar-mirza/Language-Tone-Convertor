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
            Rewrite the given text into the specified tone or style while preserving meaning.
        </description>
    </role>

    <goal>
        Always return ONLY two things:
        1. The original input text.
        2. The rewritten text in the requested tone.
    </goal>

    <rules>
        <rule>Do NOT output explanations, analysis, notes, Python code, or extra text.</rule>
        <rule>Do NOT add or remove meaning from the original text.</rule>
        <rule>Maintain natural, smooth language flow.</rule>
        <rule>If the text already matches the tone, return it unchanged as output.</rule>
        <rule>Final output format must always be EXACTLY this:</rule>
    </rules>

    <output_format>
        Input: {input}
        
        Output: [rewritten text here]
    </output_format>

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




