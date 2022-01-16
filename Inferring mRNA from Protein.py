
codon_map = {
    'UUU': 'F',     'CUU': 'L',     'AUU': 'I',     'GUU': 'V',
    'UUC': 'F',     'CUC': 'L',     'AUC': 'I',     'GUC': 'V',
    'UUA': 'L',     'CUA': 'L',     'AUA': 'I',     'GUA': 'V',
    'UUG': 'L',     'CUG': 'L',     'AUG': 'M',     'GUG': 'V',
    'UCU': 'S',     'CCU': 'P',     'ACU': 'T',     'GCU': 'A',
    'UCC': 'S',     'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'UCA': 'S',     'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'UCG': 'S',     'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'UAU': 'Y',     'CAU': 'H',     'AAU': 'N',     'GAU': 'D',
    'UAC': 'Y',     'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'UAA': 'Stop',  'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'UAG': 'Stop',  'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'UGU': 'C',     'CGU': 'R',     'AGU': 'S',     'GGU': 'G',
    'UGC': 'C',     'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'UGA': 'Stop',  'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'UGG': 'W',     'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}
with open('aa_sequence.txt') as file: 
    aa_sequence = file.read().strip()



def codon_frequency(): #kodonların sıklığını hesaplayan fonksiyon
    frequency = {} #frequency isminde bir map oluşturuyoruz
    for k, v in codon_map.items(): #codon_map'i for ile tarıyoruz
        if v in frequency: 
             frequency[v] = frequency[v] + 1  #  varsa value değerini 1 arttırıyoruz
        else:
            frequency[v] = 1 #eğer o frequency mapinde o anki codon_map'in key değeri yoksa oluşturup value değerine 1 atıyoruz. Kontrol için yapıyoruz.
    print(frequency) # frequency çıktılarının değerleri 
    return frequency # frequency mapini döndürüyoruz


def possible_sequences(sequence): # mümkün olan sequences'i hesaplayan foksiyon
    f = codon_frequency() #kodon frekansını f'ye atıyoruz 
    n = f['Stop'] # stop'un sıklığını n'ye atıyrouz
    for seq in sequence: # sekansın içinde gezmek için for döngüsü açıyoruz
        n = n* f[seq] # n ile for dan gelen değeri çarpıp n'ye atıyoruz. 
    return (n % 1000000) # 1000000 göre modulü alınıp değeri döndürüyoruz. 
    
print(possible_sequences(aa_sequence)) # Proteinin çevrilmiş olabileceği farklı RNA dizilerinin toplam sayısının çıktısı


    