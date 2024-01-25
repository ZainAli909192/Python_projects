import pywhatkit as pw
txt="""

Problem
The use of vehicles increasing day by day as a result road accidents are also increasing. Approximately 3,700 people die every day in road accidents worldwide, making a total of 1.35 million deaths globally in a year. This death is because of no prior exact information is provided about the location where accident take place at the right time. Like Sometime people face accident situation at unpopulated areas where nobody can help them specially on night. As a result, victims most of the time die due to not getting medical aid on time. So road accident is a very serious and critical issue that people face.


"""
pw.text_to_handwriting(txt,"demo2.png",[255,255,255])
print("Successfully converted text")