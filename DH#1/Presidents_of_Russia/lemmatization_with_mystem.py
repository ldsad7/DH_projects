import os

def main():
    for d, dirs, files in os.walk('corpus'):
        for f in files:
            output = os.path.join('corpus', 'lemmatized', f)
            f_ = os.path.join('corpus', f)
            os.system('mystem.exe' + ' ' + f_ + ' ' + output + ' ' + '-nld')
            print(f_, output)

if __name__ == '__main__':
    main()
