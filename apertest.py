
def get_translations(start=0, end=1, type='mt'):
    from Data import Data
    dataset = Data().get_data()
    out = []
    if type == 'mt':
        for a in range(start, end):
            out.append(dataset[a][1])
        return out
    else:
        for a in range(start, end):
            out.append(dataset[a][2])
        return out


def words_to_vec(x, val=True, remove_text=False):
    from WordEmbeddings import WordEmbeddings
    out = []
    for a in x:
        out.append(WordEmbeddings(text=a).get_spanish_vectors(
            normalized=val, remove_text=remove_text))
    return out


mt = get_translations(start=0, end=6, type='mt')

mt_v = words_to_vec(mt[0], remove_text=True)

final = zip(mt_v, mt)

print(final)
