import openai

openai.api_key = "your api key"

output = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{"role":"system", "content":"you are an CEO in a artificial intelligence company"},
              {"role":"system", "content":"you are an CEO in a artificial intelligence company"},
              {"role":"assistant", "content":"""There are several top colleges and universities known for their programs and research in the field of artificial intelligence. Some of these institutions
               include:\n\n1. Massachusetts Institute of Technology (MIT) - Department of Electrical Engineering and Computer Science: MIT is renowned for its cutting-edge research in AI and offers
various AI-related programs and courses.\n\n2. Stanford University - Computer Science Department: Stanford has a strong AI and machine learning research community, and its CS department
offers a range of AI courses and programs.\n\n3. Carnegie Mellon University - School of Computer Science: CMU is recognized for its expertise in AI and robotics. It offers programs
such as the Machine Learning Department and the Language Technologies Institute.\n\n4. University of California, Berkeley - Berkeley Artificial Intelligence Research (BAIR)
Laboratory: UC Berkeley has highly regarded research groups in AI, and BAIR provides a collaborative environment for AI research.\n\n5. University of Oxford - Department of Computer
Science: Oxford has a well-respected AI research community and offers various AI-related programs and courses, including the Oxford Machine Learning Research Group.\n\n6. University
of Cambridge - Department of Computer Science and Technology: Cambridge has a strong AI research community and offers programs and initiatives focused on AI, such as the Leverhulme
Centre for the Future of Intelligence.\n\n7. University of Toronto - Department of Computer Science: The University of Toronto has prominent research groups in AI, including the 
Vector Institute for Artificial Intelligence, which offers interdisciplinary programs and collaborative research.\n\n8. ETH Zurich - Department of Computer Science: ETH Zurich is
known for its research in AI and offers programs such as the Master's in Robotics, Systems, and Control, which includes AI-related courses and research opportunities.\n\nThese are
just a few examples, but many other universities and research institutions have reputable AI programs and research groups. It is important to explore individual university websites, review faculty profiles, and consider specific research areas of interest to find the best fit for your AI education."""},
              {"role":"user", "content":"tell me what will be the average tuition fee for me to study in these colleges"}]
)
print(output["choices"][0]["message"]["content"])
print(output)