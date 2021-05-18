from django.db import models



DEPART_CHOICES =  (('mech','MECHANICAL'),
                    ('cs','CS'),
                    ('it', 'IT'),
                    ('bio', 'biomedical'),
                    ('eee', 'EEE'),
                    ('civil', 'CIVIL')
        
)    


YEAR_ID =  (('1','1st year'),
                    ('2','2nd year'),
                    ('3', '3rd year'),
                    ('4', '4t year')
                    
)
ACADEMIC_YEAR_ID = (('1','1st year'),
('2','2nd year'),
('3', '3rd year'),
('4', '4t year')
)

SUB_CHOICES = (('HMT', 'Heat and Mass Transfer'),
('EE', 'English for Engineers'),
('RES', 'Renewable Energy Source'),
('SE', 'Software Engineers'),
('ST', 'Software Testing'),
('POM', 'Principle of management'),
('NT', 'Nano Technology'),
('MSWM', 'Municipal Solid Waste Management')

) 





class student(models.Model):
    name = models.CharField(max_length = 50 , primary_key = True )
    age =  models.IntegerField()
    email = models.CharField(max_length = 50 )
    phone = models.CharField(max_length = 12 )
   

    def __str__(self):
        return self.name




class depart(models.Model):
    name = models.CharField(max_length =20)
    department = models.CharField(max_length= 6, choices = DEPART_CHOICES, unique = True)
    year = models.CharField(max_length =20, choices = YEAR_ID, unique = True  , primary_key =True)

class course(models.Model):
    year =  models.CharField(max_length  = 20, choices = ACADEMIC_YEAR_ID)  
    courses = models.CharField(max_length =15, choices =SUB_CHOICES)  

