from DataProcess.ProcessData import process_data
from TempleteMapping.extract_allidxjson import extract_all

def main():
    extract_all('./data/RawData/USPTO-50k', './data/ProcessedData/USPTO-50k')

    pd = process_data('./data/RawData/USPTO-50k', './data/ProcessedData/USPTO-50k')
    pd.process()


if __name__ == '__main__':
    main()