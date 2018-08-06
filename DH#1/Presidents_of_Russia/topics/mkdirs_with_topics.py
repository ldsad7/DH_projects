import re, os

def main():
    with open('output_direct_lines.txt', 'r', encoding="utf-8") as g:
        topics = g.read().split('________________________________________')
        for i in range(len(topics)):
            topics[i] = topics[i].split('\n')[1:-1]
            print(topics[i])
    
    with open('matching_docs_with_topics.txt', 'r', encoding="utf-8") as f:
        i = 0
        for line in f.readlines():
            year = re.findall('pl\/(.*?)\.txt', line)[0]
            for k in range(5):
                with open(os.path.join('corpus', str(k) + '_' + year + '.txt'), 'w', encoding="utf-8") as t:
                    t.write(topics[i][k].split('\t')[2])
            i += 1
            
if __name__ == '__main__':
    main()
