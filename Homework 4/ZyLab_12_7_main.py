# Saqib Siddiqui
# PSID: 1495537


def get_age():
        patient_age = int(input())
        if (patient_age) < 18 or (patient_age > 75):
            raise ValueError('Invalid age.')
        return patient_age

def fat_burning_heart_rate(patient_age):
    return(0.7*(220-patient_age))

if __name__ == '__main__' :
    try:
        get_age = get_age()
        print('Fat burning heart rate for a',get_age,'year-old:',fat_burning_heart_rate(get_age),'bpm')
    except ValueError as excpt:
        print(excpt)
        print('Could not calculate heart rate info.\n')







