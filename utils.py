import os


def _parse_file_name(file_name: str, option: str):
    components = file_name.split(option)
    return components[0]


def get_math_proofs(math_concept: str) -> list:
    proofs = []

    if math_concept == 'calc_1':
        for root, directory, files in os.walk("static"):
            for file in files:
                if 'calc_1' in file:
                    proof_name = _parse_file_name(file, 'calc_1')
                    proofs.append({
                        'proof_name': proof_name,
                        'src': "static/" + file
                    })

        return proofs
    elif math_concept == 'calc_2':
        return ["Reimann's Sum II", "Sigma delta proof II", "Delta Epsilon II", "God of War", 'Death Stranding',
                'Chiptole', 'Communism', 'ff', 'Bruh moment']
    else:
        return ['Theorem IIII']


print(get_math_proofs('calc_1'))

proofs = get_math_proofs('calc_1')

for i in range(len(proofs)):
    print(proofs[i]['proof_name'])
