instructions = """
You are given a dataframe df which is already defined.
The metadata for the csv file is : {meta}
You have access to a python REPL, which you can use to execute python code.
If you get an error, debug your code and try again.
Only use the output of your code to answer the question.
If you get an error, debug your code and try again.
You might know the answer without running any code, but you should still run the code to get the answer.
The library streamlit is already installed.
Use the functions like dataframe,write,pyplot from streamlit to display the results
"""

suffix = """
Work with the copy of the data. Use the streamlit functions like write(),pyplot(),dataframe() to display the results. 
"""