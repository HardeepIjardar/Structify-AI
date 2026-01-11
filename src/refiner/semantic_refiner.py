from src.models import RefinedIntent


class SemanticRefiner:
    async def refine(self, text: str) -> RefinedIntent:
        lowered = text.lower()

        motivational_keywords = [
            "amazing", "great job", "keep going", "awesome",
            "fantastic", "well done", "you got this"
        ]

        if any(k in lowered for k in motivational_keywords):
            return RefinedIntent(
                primary_goal="none",
                problem_statement="Non-actionable input",
                target_user="none",
                requirements=[],
                technical_constraints=[],
                business_constraints=[],
                design_constraints=[],
                deliverables=[],
                output_format="",
                open_questions=[],
                confidence_score=0.1,
            )

        # Default actionable stub
        return RefinedIntent(
            primary_goal="Build a simple system",
            problem_statement="Need to organize functionality",
            target_user="General users",
            requirements=[{"description": "Basic feature", "priority": "must"}],
            technical_constraints=[],
            business_constraints=[],
            design_constraints=[],
            deliverables=["Working system"],
            output_format="Web application",
            open_questions=["Exact scope unclear"],
            confidence_score=0.5,
        )
