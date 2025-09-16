# STRUCTURED OUTPUT
# In LangChain, structured output refers to the practice of having language models return
# responses in a well-defined data format (for example, JSON), rather than free-form text. This
# makes the model output easier to parse and work with programmatically.


# Why Structured Data
# Data Extraction, API building, Agents

# There are some models who are capable of giving structured out and some arent

# capable models=> we have with_structured_output() in langchaing
# incapable=> output parser



# Three ways of achieving struct data in capable models -> typeddict,pydantic,json

# TYPEDDICT
# TypedDict is a way to define a dictionary in Python where you specify what keys and values
# should exist. It helps ensure that your dictionary follows a specific structure.
# Why use TypedDict?
# • It tells Python what keys are required and what types of values they should have.
# • It does not validate data at runtime (it just helps with type hints for better coding).

#PYDANTIC
# Pydantic is a data validation and data parsing library for Python. It ensures that the data you
# work with is correct, structured, and type-safe.

#json