from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError, ModelForm

from utils.valida_cep import consulta_cep
from utils.validador_cpf import valida_cpf

class Perfil(models.Model):
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
        
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    idade = models.PositiveIntegerField(blank= True, null= True)
    data_nascimento = models.DateField(blank= True, null= True)
    cpf = models.CharField(max_length= 11)
    cep = models.CharField(max_length= 8)
    endereco = models.CharField(max_length= 50, blank= True)
    numero = models.CharField(max_length= 5)
    bairro = models.CharField(max_length= 30, blank= True)
    cidade = models.CharField(max_length= 30, blank= True)
    complemento = models.CharField(max_length= 30, blank= True)
    estado = models.CharField(
        default= 'AC',
        max_length= 2,
        choices= (
            ('AC', 'Acre'),
            ('AL', 'Alagoas'),
            ('AP', 'Amapá'),
            ('AM', 'Amazonas'),
            ('BA', 'Bahia'),
            ('CE', 'Ceará'),
            ('DF', 'Distrito Federal'),
            ('ES', 'Espírito Santo'),
            ('GO', 'Goiás'),
            ('MA', 'Maranhão'),
            ('MT', 'Mato Grosso'),
            ('MS', 'Mato Grosso do Sul'),
            ('MG', 'Minas Gerais'),
            ('PA', 'Pará'),
            ('PB', 'Paraíba'),
            ('PR', 'Paraná'),
            ('PE', 'Pernambuco'),
            ('PI', 'Piauí'),
            ('RJ', 'Rio de Janeiro'),
            ('RN', 'Rio Grande do Norte'),
            ('RS', 'Rio Grande do Sul'),
            ('RO', 'Rondônia'),
            ('RR', 'Roraima'),
            ('SC', 'Santa Catarina'),
            ('SP', 'São Paulo'),
            ('SE', 'Sergipe'),
            ('TO', 'Tocantinsa'),
        )
    )
    def __str__(self) -> str:
        return f'{self.usuario}'
    
    def clean(self):
        error_messages = {}
        cep = consulta_cep(self.cep)
        if not valida_cpf (self.cpf):
            error_messages['cpf'] = 'Digite um CPF válido'
        
        if not cep:
            error_messages['cep'] = 'Digite um CEP válido'
        else:
            self.bairro = cep['bairro']
            self.endereco = cep['end']
            self.cidade = cep['cidade']
            self.estado = cep['uf']
        if error_messages:
            raise ValidationError(error_messages)
    
# class PerfilForm(ModelForm):
#     models = Perfil

#     def save(self, commit=True):
#         if not PerfilForm.is_valid:
#             form_instance = super(PerfilForm, self).save(commit=False)
#             cleaned_data = self.cleaned_data
#             cleaned_data['endereco']
#             cleaned_data['bairro']
#             cleaned_data['cidade']
#             cleaned_data['estado']
#             if commit:
#                 form_instance.save()
#             return form_instance
        
   