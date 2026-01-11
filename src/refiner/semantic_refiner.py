from src.models import RefinedIntent


class SemanticRefiner:
    async def refine(self, text: str) -> RefinedIntent:
        lowered = text.lower()

        # Hard reject: non-actionable chatter
        motivational_keywords = [
            "amazing", "great job", "keep going", "awesome",
            "fantastic", "well done", "you got this"
        ]

        if any(k in lowered for k in motivational_keywords):
            return RefinedIntent(
                primary_goal="none",
                problem_statement="Non-actionable motivational input",
                target_user="none",
                requirements=[],
                technical_constraints=[],
                business_constraints=[],
                design_constraints=[],
                deliverables=[],
                output_format="",
                open_questions=["No actionable intent detected"],
                confidence_score=0.1,
            )

        # Feature extraction
        feature_keywords = {
            "auth": "User authentication",
            "login": "User login",
            "dashboard": "Dashboard view",
            "notification": "Notifications",
            "role": "Role-based access",
            "admin": "Admin controls",
            "status": "Status tracking",
            "deadline": "Deadline management",
            "report": "Reporting",
        }

        requirements = []
        for k, desc in feature_keywords.items():
            if k in lowered:
                requirements.append({
                    "description": desc,
                    "priority": "must"
                })

        ambiguities = []
        if "simple" in lowered or "basic" in lowered:
            ambiguities.append("Scope definition unclear")

        architecture_signals = [
            "rest",
            "api",
            "backend",
            "frontend",
            "web-based",
            "browser-based",
            "service"
        ]

        if "system" in lowered and not any(a in lowered for a in architecture_signals):
            ambiguities.append("Architecture unspecified")


        # Confidence calculation
        confidence = 0.3
        confidence += min(len(requirements) * 0.1, 0.4)
        confidence -= min(len(ambiguities) * 0.1, 0.3)
        confidence = max(0.0, min(confidence, 1.0))
        # Scope clarity boosters
        if "small team" in lowered or "small teams" in lowered or "under 50 users" in lowered:
            confidence += 0.1

        if "no mobile" in lowered or "no mobile support" in lowered:
            confidence += 0.1

        confidence = min(confidence, 1.0)



        return RefinedIntent(
            primary_goal="Build a software system",
            problem_statement="User described a system to be built",
            target_user="End users",
            requirements=requirements,
            technical_constraints=[],
            business_constraints=[],
            design_constraints=[],
            deliverables=["Working application"],
            output_format="Web application",
            open_questions=ambiguities,
            confidence_score=confidence,
        )
