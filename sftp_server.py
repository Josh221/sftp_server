#Import required modules.
import paramiko

#Function to handle the file transfers.
def transfer_file(local_path, remote_path, mode='put'):
    #Open the secure file transfer protocol
    sftp = ssh.open_sftp()
    
    #If user selected put then upload file from local path entered to remote path on server
    if mode == 'put':
        #Try to download file from remote server
        try:  
            sftp.put(local_path, remote_path)
            #Show confirmation to user once complete successfully
            print(f"File '{local_path}' uploaded to '{remote_path}' successfully.")
        except:
            #If file transfer fails show user feedback
            print("File transfer failed. Please try again.")
    #If user selected get then download file from remote path entered to local path on pc       
    elif mode == 'get':
        #Try to download file from remote server
        try:
            sftp.get(remote_path, local_path)
            #Show confirmation to user once complete successfully
            print(f"File '{remote_path}' downloaded to '{local_path}' successfully.")
        except: 
            #If file transfer fails show user feedback
            print("File transfer failed. Please try again.")

    #Close the SFTP
    sftp.close()

#Prompt user for remote server credentials:
#Enter server hostname/IP address
host = input("Host: ")
#Enter server username
username = input("Username: ")
#Enter server password
password = input("Password: ")

#Connect to the remote server using paramiko module
ssh = paramiko.SSHClient()
#Add automatically host_key to known_hosts
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#Connect to server via secure shell
ssh.connect(host, username=username, password=password)

# Run the file transfer process
while True:
    #Ask user whether they want to upload or download a file to the server
    command = input("Enter 'put' to upload a file or 'get' to download a file (or 'exit' to quit): ")
    #Prompt user to enter respectable file paths then validate paths, else exit
    if command == 'put':
        try:
            local_file = input("Enter the local file path: ")
            remote_file = input("Enter the remote file path: ")
            #Call function to transfer files, passing through file paths and mode
            transfer_file(local_file, remote_file, mode='put')
        except:
            print('Invalid file path, try again: ')
            
    elif command == 'get':
        try:
            remote_file = input("Enter the remote file path: ")
            local_file = input("Enter the local file path: ")
            #Call function to transfer files, passing through file paths and mode
            transfer_file(local_file, remote_file, mode='get')
        except:
            print('Invalid file path, try again: ')  

    elif command == 'exit':
        #Break loop
        break
    else:
        print("Invalid command. Please try again.")

# Close the SSH connection
ssh.close()