import os
import requests
import git
from datetime import datetime

# Konfigurasi
REPO_PATH = '/home/wahyu/webhook/zapier1/'  # Ganti dengan path ke repositori lokal Anda
GITHUB_URL = 'https://github.com/haikalazmir/webhook/blob/main/zapier1/data.txt'
FILE_PATH = 'zapier1/data.txt'  # Path relatif file yang akan diupdate di repositori lokal Anda
BRANCH = 'main'  # Nama branch Git

# Mendownload file terbaru dari GitHub
response = requests.get(GITHUB_URL)
if response.status_code == 200:
    with open(os.path.join(REPO_PATH, FILE_PATH), 'wb') as file:
        file.write(response.content)
    print(f'File {FILE_PATH} berhasil diperbarui!')
else:
    print('Gagal mengunduh file data.txt')

# Melakukan commit dan push ke GitHub
try:
    # Membuka repositori Git lokal
    repo = git.Repo(REPO_PATH)

    # Memastikan branch yang benar
    repo.git.checkout(BRANCH)

    # Menambahkan perubahan ke staging area
    repo.git.add(FILE_PATH)

    # Commit perubahan
    commit_message = f'Update data.txt pada {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}'
    repo.git.commit(m=commit_message)

    # Melakukan push ke GitHub
    repo.git.push('origin', BRANCH)
    print(f'Perubahan telah berhasil dipush ke {BRANCH}!')
except Exception as e:
    print(f'Error saat melakukan commit dan push: {e}')
