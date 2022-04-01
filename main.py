import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb') 
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BE41BwkeMYyVyx7IsR5NfNLrmJkUOQtnZwLBHmcrQlWO_CL-j1uUH-kefC3q_ip8bpv0iJKVFmhlOhu_vbodbYMug0df1WvjN-IPBKiYAPpph1kvGyOj3qrJdzkz3jGJ-Z9K2Ydg8heR'
    transferData = TransferData(access_token)

    file_from=input('Enter the file path to transfer')
    file_to=input('Enter the destination path')

    #file_from = 'test.txt'
    #file_to = '/test_dropbox/test.txt'  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File has been moved.")

if __name__ == '__main__':
    main()
