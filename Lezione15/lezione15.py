
# Esercizio 1


class FileManager:


    def __init__(self, file_name, mode):

        self.file_name = file_name
        self.mode = mode


    def __enter__(self):

        self.file_wrapper = open(self.file_name,self.mode)

        return self.file_wrapper

    def __exit__(self, exc_type, exc_value, traceback):

        self.file_wrapper.close()


with FileManager(file_name = 'prova.txt', mode = 'w') as file:

    file.write('ciao')


# Esercizio 2


class Timer:

    def __enter__(self):
        import time

        self.time = time.time()

    
    def __exit__(self, exc_type, exc_value, traceback):
        import time

        print(f"Time Elapsed: {time.time() - self.time}")

        return False
