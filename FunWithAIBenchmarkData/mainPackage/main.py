# main.py
# Bill Nicholson
# nicholdw@ucmail.uc.edu

from chartPackage.chart import LetterFrequency
from readingLevelPackage.readingLevel import Reading_Level
from utilitiesPackage.utilities import *
from utilitiesPackage.CSV_Utilities import *
from PDFPackage.PDFUtilities import *
from imagePackage.image import *
from chartPackage.chart import *

if __name__ == "__main__":
    #Team Image Generator
    image_url = "https://img.pokemondb.net/artwork/large/parasect.jpg"
    image_fetcher = ImageFetcher(url=image_url, size=(200, 200), save_path="parasect_200x200.png")
    image_fetcher.fetch_and_process_image()

    #Chart Generator
    file_path = r"C:\Users\Abel\source\repos\yemaneag_Assignment088\FunWithAIBenchmarkData\dataPackage\MMLU\data\nutrition_test.csv"
    letterfreq = LetterFrequency(file_path)
    letterfreq.display_data()
    letterfreq.plot_letter_frequency()


    CSV_Processor = MMLU_CSV_Processor("dataPackage/MMLU/data/", ["management_test.csv"])
    questions = CSV_Processor.read_data()
    print(len(questions), "questions read")

 
    myPDF = PDFUtilities()
    myPDF.create_question_PDF("Management Test", "MMLU", questions)
   
    print("The first question:")
    print(questions[0])
    
    text = convert_dictionaries_to_string(questions, ["prompt", "possible answers"])
    #print("\ntext from dictionaries:", text[0:500])

    #0. Append all the prompts into a big string - See utilities.convert_dictionaries_to_string()
    
    
    #1. Perform reading level analysis on the big string and print the results to the console.
    Reading_Level.compute_readability_indices("MMLU", text)

    #2. Process the big string to find the longest word


    #3. Process the big string to find the most prevalent word
    

    #4. Use the VS debugger: set a breakpoint somewhere to pause the project when a prompt containing the word "PEST" is read from the original CSV file
    

    #5. Perform some data visualization on the text. Research Data Vis libraries and apply one.
     

    #6a. Write all the questions and possible answers (without the correct answer) to a text file. Use a CSV format and create a unique identifier field for each question.
    #6b. Write the question identifier (see 6a, above) and the correct answer to another text file. Use a CSV format.
    questions_written = write_questions_to_text_files("MMLU", questions)
    print(questions_written, "questions written to the file.")
    
    """
    # This code is commented out
    #Reading_Level.test01()

    text = "This is a sentence that we can use to test the reading level computations. "
    reading_level_indices = Reading_Level.compute_readability_indices("Dummy Benchmark", text)
    for key in reading_level_indices.keys():
        print(key, ":", reading_level_indices[key])
            
    # A test with text at a higher reading level
    text = "Birds, employing a combination of aerodynamic principles and specialized anatomical adaptations, achieve flight through the generation of lift, which counteracts the force of gravity."
    reading_level_indices = Reading_Level.compute_readability_indices("Dummy Benchmark", text)
    for key in reading_level_indices.keys():
        print(key, ":", reading_level_indices[key])
    """
