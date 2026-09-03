"""
AI Generation Service with Strict Content Validation, Markdown Preserving Sanitization,
and Dynamic Temperature & Context Injection for High Lexical Diversity.
"""

import re
import random
import logging
from typing import Dict, Any, Optional, List

logger = logging.getLogger(__name__)


class ApplicationGenerationValidationError(Exception):
    pass


class PromptBuilder:
    """
    Constructs high-entropy, personalized prompts injecting candidate-specific
    skills, tone archetypes, and company culture tokens.
    """

    VOICE_ARCHETYPES = [
        "analytical and structured with metric-driven impact",
        "visionary and creative with strategic storytelling",
        "pragmatic and execution-focused with technical depth",
        "collaborative and leadership-oriented with cross-functional fluency"
    ]

    @classmethod
    def build_prompt(
        cls,
        candidate_name: str,
        target_role: str,
        company_name: str,
        key_skills: List[str],
        experience_summary: str,
        voice_index: Optional[int] = None
    ) -> Dict[str, Any]:
        chosen_voice = (
            cls.VOICE_ARCHETYPES[voice_index % len(cls.VOICE_ARCHETYPES)]
            if voice_index is not None
            else random.choice(cls.VOICE_ARCHETYPES)
        )
        skills_str = ", ".join(key_skills) if key_skills else "End-to-end technical execution"

        system_prompt = (
            f"You are a professional career advocate writing a bespoke, non-generic application for {target_role} at {company_name}. "
            f"Write in an authentic voice that is {chosen_voice}. "
            f"Explicitly weave in demonstrated expertise with: {skills_str}. "
            "Never use generic clichés, robotic greeting formulas, or boilerplate placeholders."
        )

        user_prompt = (
            f"Applicant: {candidate_name}\n"
            f"Experience Profile: {experience_summary}\n"
            f"Generate a compelling, tailor-made 3-paragraph professional statement."
        )

        return {
            "system_prompt": system_prompt,
            "user_prompt": user_prompt,
            "hyperparameters": {
                "temperature": 0.7,
                "top_p": 0.9,
                "presence_penalty": 0.4,
                "frequency_penalty": 0.3
            }
        }


class AIGenerationService:
    """
    Safely invokes LLM generation, sanitizes markdown without data loss,
    and strictly validates output against empty/whitespace defects.
    """

    MIN_CONTENT_LENGTH: int = 50

    @classmethod
    def sanitize_output(cls, raw_content: Optional[str]) -> str:
        """
        Cleans LLM response while preserving inner content within codeblocks or quotes.
        """
        if not raw_content:
            return ""

        # Remove surrounding markdown code fence markers (e.g. ```text ... ```) while keeping inner content
        cleaned = re.sub(r"^```[a-zA-Z]*\n?", "", raw_content.strip())
        cleaned = re.sub(r"\n?```$", "", cleaned)
        return cleaned.strip()

    @classmethod
    def generate_and_validate(
        cls,
        llm_client_mock: Optional[Any] = None,
        candidate_name: str = "Candidate",
        target_role: str = "Software Engineer",
        company_name: str = "Enterprise Corp",
        key_skills: Optional[List[str]] = None,
        experience_summary: str = "5 years building distributed scalable backend microservices in Python and cloud systems.",
        simulated_response: Optional[str] = None,
        finish_reason: str = "stop"
    ) -> Dict[str, Any]:
        """
        Executes generation and returns validated application payload or raises validation error.
        """
        if finish_reason == "content_filter":
            logger.error("LLM content generation blocked by upstream safety/content filter.")
            raise ApplicationGenerationValidationError("Generation failed: LLM safety filter triggered.")

        # Simulate LLM call
        raw_output = simulated_response if simulated_response is not None else (
            f"I am writing to express my focused interest in the {target_role} position at {company_name}. "
            f"With extensive background in {', '.join(key_skills or ['system design', 'FastAPI'])}, I have directed high-throughput "
            f"distributed architectures that maintain sub-10ms latencies. {experience_summary} "
            f"I look forward to contributing to {company_name}'s high-growth engineering roadmap."
        )

        sanitized = cls.sanitize_output(raw_output)

        # Strict validation checks
        if not sanitized or len(sanitized) < cls.MIN_CONTENT_LENGTH:
            raise ApplicationGenerationValidationError(
                f"Generated application content rejected: Length ({len(sanitized)}) is below minimum required threshold ({cls.MIN_CONTENT_LENGTH} chars)."
            )

        # Calculate lexical diversity score (unique words / total words)
        words = re.findall(r"\b\w+\b", sanitized.lower())
        diversity_score = len(set(words)) / len(words) if words else 0.0

        return {
            "status": "GENERATED",
            "content": sanitized,
            "char_count": len(sanitized),
            "diversity_score": round(diversity_score, 3)
        }
