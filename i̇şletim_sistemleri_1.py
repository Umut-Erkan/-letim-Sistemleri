
#Child Process Oluşturma ve Yönetimi
import os
def file_read():
	file_to_read = "/content/example.txt"
	#execlp komutu ile dosya okuma.
	os.execlp("cat", "cat", file_to_read)

def parent_child():
	n = os.fork()

	# n 0'dan büyükse parent procces demek.
	if n > 0:
		print("Parent process and id is : ", os.getpid())
		child_pid, status = os.wait()

		ex_code = os.WEXITSTATUS(status)

		if os.WIFEXITED(status):
			print(f"Alt işlem tamamlandı. PID: {child_pid}, Çıkış kodu:{ex_code}")

		else:
			 print(f"Alt işlem beklenmedik şekilde sonlandı. PID: {child_pid}")

	# n 0'a eşitse child procces demek.
	if n==0 :
		print("Child process and id is : ", os.getpid())
		#file_read()

parent_child()

#file_read()

#Child Process’lerde Hata Yönetimi
import os
file_path = "example.txt"

if os.path.exists(file_path):
    print(f"Dosya mevcut: {file_path}")
    with open(file_path, "r") as file:
        print("Dosya içeriği:",file.read())
else:
    print(f"Dosya mevcut değil: {file_path}")

def open_file(file_path):
    with open(file_path, "r") as file:
        print(f"Dosya içeriği ({file_path}):")
        print(file.read())


def parent_child():
    file_path = "example.txt"

    n = os.fork()  # Yeni bir child process oluştur
    if n > 0:  # Parent process
        print(f"Parent process çalışıyor. ID: {os.getpid()}")
        child_pid, status = os.wait()  # Child process'i bekle
        if os.WIFEXITED(status):
            exit_code = os.WEXITSTATUS(status)
            print(f"Child process tamamlandı. PID: {child_pid}, Çıkış kodu: {exit_code}")
        else:
            print(f"Child process beklenmedik şekilde sonlandı. PID: {child_pid}")
    else:  # Child process
        print(f"Child process çalışıyor. ID: {os.getpid()}")
        open_file(file_path)  # Dosyayı aç ve oku
        os._exit(0)  # Başarıyla çık

parent_child()