from azure.communication.email import EmailClient, EmailContent, EmailAddress, EmailMessage, EmailRecipients
connection_string = ""
client = EmailClient.from_connection_string(connection_string);

content = EmailContent(
        subject="Felicitari! Ati incarcat un videoclip!",
        plain_text="Pentru a ridica castigul, va rugam sa il contactati pe radu.codreanu@s.unibuc.ro",
        html= "<html><h1>Radu Stefan Codreanul va va asista daca nu reusiti sa accesati thumbnail-ul liviu.albei@s.unibuc.ro/cojocaru.andrei.3@s.unibuc.ro/radu.codreanu@s.unibuc.ro!</h1></html>",
)

with open('/var/www/uploads/emailurile_kober.txt', 'r') as citirea:
        emailul = citirea.read()

address = EmailAddress(email=emailul, display_name="Orlandoooo")
message = EmailMessage(
        sender="DoNotReply@",
        content=content,
        recipients=EmailRecipients(to=[address])
)
response = client.send(message)
print(response)
