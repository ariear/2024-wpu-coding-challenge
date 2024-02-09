def get_grade(s1, s2, s3):
    averange = (s1 + s2 + s3) / 3
    if averange >= 90 and averange <= 100:
        return 'A'
    elif averange >= 80 and averange < 90:
        return 'B'
    elif averange >= 70 and averange < 80:
        return 'C'
    elif averange >= 60 and averange < 70:
        return 'D'
    else:
        return 'F'
