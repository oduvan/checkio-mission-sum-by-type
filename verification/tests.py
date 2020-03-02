"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [[]],
            "answer": ['', 0],
        },
        {
            "input": [[1,2,3]],
            "answer": ['', 6],
        },
        {
            "input": [['1',2,3]],
            "answer": ['1', 5],
        },
        {
            "input": [['1','2',3]],
            "answer": ['12', 3],
        },
        {
            "input": [['1','2','3']],
            "answer": ['123', 0],
        },
        {
            "input": [['size', 12, 'in', 45, 0]],
            "answer": ['sizein', 57],
        }
    ],
    "Extra": [
        {
            "input": [['hello',' ', 'world']],
            "answer": ['hello world', 0],
        },
        {
            "input": [[1,2,3,4,5, 'and', 6]],
            "answer": ['and', 21],
        }
    ]
}
