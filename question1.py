import json

def countWords_1(filename, result):
    text = open(filename, "r")
    d = dict()

    for line in text: 
        line = line.strip()
        line = line.lower()
        words = line.split()

    for word in words: 
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1 


    json_object = json.dumps(d, indent=len(d))
    with open(result, "w") as outfile:
      outfile.write(json_object)
    

    
# Driver function
if __name__ == "__main__":
    samplefile = "Sample_Inputs/sample.txt"
    result = "OutputFile/result1.json"

countWords_1(samplefile, result)


