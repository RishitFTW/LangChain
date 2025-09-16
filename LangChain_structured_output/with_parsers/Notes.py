# Output Parsers
# Output Parsers in LangChain help convert raw LLM responses into structured formats like
# JSON, CSV, Pydantic models, and more. They ensure consistency, validation, and ease of use in
# applications.

# Most Used Op Parsers

# String Op Parser
# allows us the parse llm response into string no need to response.content. Useful with Chains

# Json Op Parser
# returns the response in JSON format but doesnt enforce the schema

# Structured Op Parser
# returns the response in Structured JSON but no data Validation

# pydantic op parser
# returns schema validated structured JSON