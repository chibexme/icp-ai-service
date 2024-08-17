from pydantic import BaseModel

from schema import GrammarAnalysisRequest


class GrammarAnalysis(BaseModel):
    grammatical_errors: str = "None"
    syntactic_errors: str = "None"
    general_suggestions: str
    rewrite: str


def grammar_check():
    return {
        "type": "function",
        "function": {
            "name": "provide_grammar_check",
            "description": "Provide grammar check and rewrite of the provided text",
            "parameters": {
                "type": "object",
                "properties": {
                    "grammatical_errors": {
                        "type": "string",
                        "description": "provide a list of grammatical errors",
                    },
                    "syntactic_errors": {
                        "type": "string",
                        "description": "provide a list a syntactical errors",
                    },
                    "general_suggestions": {
                        "type": "string",
                        "description": "general suggestions to improve the text, tone, style etc.",
                    },
                    "rewrite": {
                        "type": "string",
                        "description": "rewrite the text to fix all the syntactic, grammatical errors and incorporate "
                                       "the general suggestions as well.",
                    },
                },
                "required": ["general_suggestions", "rewrite"],
            },
        },
    }


def provide_grammar_check(data: GrammarAnalysis):
    return data


def grammar_cmd(req: GrammarAnalysisRequest):
    prompt = f"Provide grammar check, suggestions and rewrite of the provided text: {req.text}"
    return prompt
