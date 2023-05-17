class CpfUtils:
    @staticmethod
    def mask_cpf(cpf: str) -> str:
        return ''

    @staticmethod
    def unmask_cpf(cpf: str) -> str:
        cpf_unmasked = cpf.replace('.', '').replace('-', '')

        return cpf_unmasked
