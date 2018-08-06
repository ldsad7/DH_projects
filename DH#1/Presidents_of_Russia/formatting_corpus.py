import os

def main():
    for d, dirs, files in os.walk('corpus'):
        for f in files:
            g = f.split('.')
            t = g[1].split('_')
            h = g[0] + '.' + t[1] + '_' + t[0] + '.txt'
            os.rename(os.path.join('corpus', f), os.path.join('corpus', h))

if __name__ == '__main__':
    main()
