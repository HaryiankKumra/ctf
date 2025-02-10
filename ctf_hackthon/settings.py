DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'ctf_hackathon',
        'CLIENT': {
            'host': 'mongodb://localhost:27017/',  # MongoDB connection string
        }
    }
}