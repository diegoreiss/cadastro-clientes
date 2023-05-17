from \
    PySide6.QtWidgets \
    import \
    QMainWindow, QLabel, QLineEdit, \
    QComboBox, QPushButton, QVBoxLayout, \
    QWidget, QSizePolicy
from PySide6.QtGui import QIntValidator
from ..Infra.Repository.cliente_repository import ClienteRepository
from ..Utils.cpf_utils import CpfUtils


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(400, 700)
        self.setWindowTitle('Cadastro de Clientes')

        self.lbl_cpf = QLabel('CPF*')
        self.txt_cpf = QLineEdit()
        self.txt_cpf.setInputMask('000.000.000-00')

        self.lbl_nome = QLabel('Nome*')
        self.txt_nome = QLineEdit()

        self.lbl_telefone_fixo = QLabel('Telefone Fixo*')
        self.txt_telefone_fixo = QLineEdit()
        self.txt_telefone_fixo.setInputMask('(00)0000-0000')

        self.lbl_telefone_celular = QLabel('Telefone Celular*')
        self.txt_telefone_celular = QLineEdit()
        self.txt_telefone_celular.setInputMask('(00)00000-0000')

        self.lbl_sexo = QLabel('Sexo')
        self.cb_sexo = QComboBox()
        self.cb_sexo.addItems(['Não Informado', 'Masculino', 'Feminino'])

        self.lbl_cep = QLabel('Cep*')
        self.txt_cep = QLineEdit()
        self.txt_cep.setInputMask('00.000-000')

        self.lbl_logradouro = QLabel('Logradouro*')
        self.txt_logradouro = QLineEdit()

        self.lbl_numero = QLabel('Número*')
        self.txt_numero = QLineEdit()
        self.txt_numero.setValidator(QIntValidator(0, 999999999))

        self.lbl_complemento = QLabel('Complemento*')
        self.txt_complemento = QLineEdit()

        self.lbl_bairro = QLabel('Bairro')
        self.txt_bairro = QLineEdit()

        self.lbl_municipio = QLabel('Município*')
        self.txt_municipio = QLineEdit()

        self.lbl_estado = QLabel('Estado*')
        self.txt_estado = QLineEdit()

        self.btn_salvar = QPushButton('Salvar')
        self.btn_limpar = QPushButton('Limpar')
        self.btn_remover = QPushButton('Deletar')

        layout = QVBoxLayout()
        layout.addWidget(self.lbl_cpf)
        layout.addWidget(self.txt_cpf)
        layout.addWidget(self.lbl_nome)
        layout.addWidget(self.txt_nome)
        layout.addWidget(self.lbl_telefone_fixo)
        layout.addWidget(self.txt_telefone_fixo)
        layout.addWidget(self.lbl_telefone_celular)
        layout.addWidget(self.txt_telefone_celular)
        layout.addWidget(self.lbl_sexo)
        layout.addWidget(self.cb_sexo)
        layout.addWidget(self.lbl_cep)
        layout.addWidget(self.txt_cep)
        layout.addWidget(self.lbl_logradouro)
        layout.addWidget(self.txt_logradouro)
        layout.addWidget(self.lbl_numero)
        layout.addWidget(self.txt_numero)
        layout.addWidget(self.lbl_complemento)
        layout.addWidget(self.txt_complemento)
        layout.addWidget(self.lbl_bairro)
        layout.addWidget(self.txt_bairro)
        layout.addWidget(self.lbl_municipio)
        layout.addWidget(self.txt_municipio)
        layout.addWidget(self.lbl_estado)
        layout.addWidget(self.txt_estado)
        layout.addWidget(self.btn_salvar)
        layout.addWidget(self.btn_limpar)
        layout.addWidget(self.btn_remover)

        self.container = QWidget()
        self.container.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setCentralWidget(self.container)
        self.container.setLayout(layout)

        self.btn_limpar.clicked.connect(self.limpar_campos)

    def salvar_cliente(self):
        ClienteRepository.insert()

    def get_all_fields(self) -> dict:
        cpf = CpfUtils.unmask_cpf(self.txt_cpf.text())

        fields = {
            'cpf': self.txt_cpf.text()
        }

        return fields


    def is_campos_cheios(self) -> bool:
        b = len(self.txt_cpf.text()) == 14 \
            and len(self.txt_nome.text()) != 0 \
            and len(self.txt_telefone_fixo.text()) == 13 \
            and len(self.txt_telefone_celular.text()) == 14 \
            and len(self.txt_cep.text()) == 10 \
            and len(self.txt_logradouro.text()) != 0 \
            and len(self.txt_numero.text()) != 0 \
            and len(self.txt_complemento.text()) != 0 \
            and len(self.txt_bairro.text()) != 0 \
            and len(self.txt_municipio.text()) != 0 \
            and len(self.txt_estado.text()) != 0

        return b

    def limpar_campos(self):
        for child in self.container.children():
            if isinstance(child, QLineEdit):
                child.clear()
            elif isinstance(child, QComboBox):
                child.setCurrentIndex(0)
