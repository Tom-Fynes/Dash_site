from enum import Enum

ALLOWED_CARD_TYPES = ["skills","projects"]

class Skills(Enum):
    PYTHON = {
        "title": "Python",
        "body":"""Using as the main language for professional development. 
                    effective in writing scalable, testable, and maintainable code.""",
        "image_path": ""
    }
    SQL_SERVER = {
        "title": "SQL Server",
        "body":"""Proficient in all areas for SQL Server database development & administration; 
                    performance tuning, indexing beack up and retores etc.""",
        "image_path": ""
    }
    AWS = {
        "title": "AWS",
        "body":"""Certified cloud practitinor with experience working with AWS on enterprise projects.""",
        "image_path": ""
    }
    TRINO = {
        "title": "Trino",
        "body":"""Experienced in creating and tuning presto sql statements.""",
        "image_path": ""
    }
    GIT = {
        "title": "Git",
        "body":"""Skilled in git and github CLI with the ability to maintain repository source control.""",
        "image_path": ""
    }
    SSRS = {
        "title": "SSIS",
        "body":"""Competent in deploying, creating and suporting SSRS reports along with
            maintaining and installing the SSRS product.""",
        "image_path": ""
    }
    POWERSHELL = {
        "title": "Powershell",
        "body":"""Proficient in writing supportable and testable powershell scripts.""",
        "image_path": ""
    }
    C_SHARP = {
        "title": "C#",
        "body":"""Previous experiance with Windows forms and WPF development, along with C# scripting.""",
        "image_path": ""
    }
    SSIS = {
        "title": "SSIS",
        "body":"""Skilled in creating and maintaining SSIS packages.""",
        "image_path": ""
    }