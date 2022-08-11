from zipfile import ZipFile
import os
import hashlib
import stat
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

archive_naked = 'Varonisa.zip'
archive_name = 'Varonica.zip'
filenames = ["Var", "Oni", "S"]
gauth = GoogleAuth()
drive = GoogleDrive(gauth)


def main():
    def pass_zip_creation():
        # Dummy files
        for filename in filenames:
            with open("{}.txt".format(filename), 'w') as f:
                f.write("Specific Cultural Diversity\n")
                f.write("Immature Colorful Profanity\n")
                f.write("Aggregate Up Until In{}anity".format(filename))
        # Write the zip to my PC, while naming it.
        with ZipFile(archive_name, 'w') as protected_archive:
            # Set password for zip file.
            protected_archive.setpassword(b"YouCanNeverGuess")
            protected_archive.write('Var.txt')
            protected_archive.write('Oni.txt')
            protected_archive.write('S.txt')
        for filename in filenames:
            os.remove(filename + ".txt")
            print(f"Removed {filename}")

    def extract_content(zipname):
        with ZipFile(zipname, mode="r") as archive:
            archive.extract(filenames[2] + ".txt", pwd=b"YouCanNeverGuess")
            my_file = filenames[2] + ".txt"
            print(f"Extracted {my_file} file")

    def shacalc(fname):
        file = fname
        sha256_hash = hashlib.sha256()
        # Set permissions, just in case...
        os.chmod(file, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        with open(file, "rb") as f:
            # Reading and updating hash value in blocks of 4k Bytes.
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
                print(sha256_hash.hexdigest())
        with open('S.txt', 'w') as includ_file_hash:
            includ_file_hash.write(sha256_hash.hexdigest())
            includ_file_hash.close()
        unprotected_varonisa = ZipFile(archive_naked, 'w')
        unprotected_varonisa.write('S.txt')
        unprotected_varonisa.close()

    def upload_files_to_drive():
        gfile = drive.CreateFile({'parents': '13h1SbQnDPrHKob_heBFjno4MyBcQBuKx'})
        gfile.SetContentFile(archive_naked)
        gfile.Upload()

    # Run functions in order
    pass_zip_creation()
    extract_content(archive_name)
    shacalc("S.txt")
    upload_files_to_drive()


# Test


if __name__ == "__main__":
    main()
