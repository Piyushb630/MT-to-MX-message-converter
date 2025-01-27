import customtkinter
from datetime import datetime


timenow = datetime.now().strftime("%H:%M:%S")

def generate_pacs009(sender, receiver, amount, currency, value_date, reference, intermediary1, intermediary2, beneficiary, beneficiaryAC, agent):
    pacs009_message = ( 
    f"<AppHdr xmlns=\"urn:iso:std:iso:20022:tech:xsd:head.001.001.01\">"
    f"<Fr>\n"
    f"    <FIId>\n"
    f"        <FinInstnId>\n"
    f"            <BICFI>{sender}</BICFI>\n"
    f"            <ClrSysMmbIßðd>\n"
    f"                <MmbId>ESSEFIHXXXXA2AFI</MmbId>\n"
    f"            </ClrSysMmbId>\n"
    f"        </FinInstnId>\n"
    f"    </FIId>\n"
    f"</Fr>\n"
    f"<To>\n"
    f"    <FIId>\n"
    f"        <FinInstnId>\n"
    f"            <BICFI>{intermediary1}</BICFI>\n"
    f"        </FinInstnId>\n"
    f"    </FIId>\n"
    f"</To>\n"
    f"<BizMsgIdr>&apos;{reference}&apos;</BizMsgIdr>\n"
    f"<MsgDefIdr>pacs.009.001.08CORE</MsgDefIdr>\n"
    f"<CreDt>{value_date}T{timenow}Z</CreDt>\n"
    f"</AppHdr>\n\n\n\n"
        
        
        
        
    f"<Document xmlns=\"urn:iso:std:iso:20022:tech:xsd:pacs.009.001.08\">\n"
    f"<FICdtTrf>\n"
    f"    <GrpHdr>\n"
    f"        <MsgId>NONREF</MsgId>\n"
    f"        <CreDtTm>{value_date}</CreDtTm>\n"
    f"        <NbOfTxs>1</NbOfTxs>\n"
    f"        <SttlmInf>\n"
    f"            <SttlmMtd>CLRG</SttlmMtd>\n"
    f"            <ClrSys>\n"
    f"                <Cd>TGT</Cd>\n"
    f"            </ClrSys>\n"
    f"        </SttlmInf>\n"
    f"    </GrpHdr>\n"
    f"    <CdtTrfTxInf>\n"
    f"        <PmtId>\n"
    f"            <InstrId>&apos;{reference}&apos;</InstrId>\n"
    f"            <EndToEndId>&apos;{reference}&apos;</EndToEndId>\n"
    f"            <UETR></UETR>\n"
    f"        </PmtId>\n"
    f"        <IntrBkSttlmAmt Ccy=\"{currency}\"/>{amount}</IntrBkSttlmAmt>\n"
    f"        <IntrBkSttlmDt>{value_date}</IntrBkSttlmDt>\n"
    f"        <SttlmPrty>NORM</SttlmPrty>\n"
    f"        <InstgAgt>\n"
    f"            <FinInstnId>\n"
    f"                <BICFI>{sender}</BICFI>\n"
    f"            </FinInstnId>\n"
    f"        </InstgAgt>\n"
    f"        <InstdAgt>\n"
    f"            <FinInstnId>\n"
    f"                <BICFI>{receiver}</BICFI>\n"
    f"            </FinInstnId>\n"
    f"        </InstdAgt>\n"
    f"        <IntrmyAgt1>\n"
    f"            <FinInstnId>\n"
    f"                <BICFI>{intermediary1}</BICFI>\n"
    f"            </FinInstnId>\n"
    f"        </IntrmyAgt1>\n"
    f"        <IntrmyAgt2>\n"
    f"            <FinInstnId>\n"
    f"                <BICFI>{intermediary2}</BICFI>\n"
    f"            </FinInstnId>\n"
    f"        </IntrmyAgt2>\n"
    f"        <Dbtr>\n"
    f"            <FinInstnId>\n"
    f"                <BICFI>{sender}</BICFI>\n"
    f"            </FinInstnId>\n"
    f"        </Dbtr>\n"
    f"        <CdtrAgt>\n"
    f"            <FinInstnId>\n"
    f"                <BICFI>{agent}</BICFI>\n"
    f"            </FinInstnId>\n"
    f"        </CdtrAgt>\n"
    f"        <Cdtr>\n"
    f"            <FinInstnId>\n"
    f"                <BICFI>{beneficiary}</BICFI>\n"
    f"            </FinInstnId>\n"
    f"        </Cdtr>\n"
    f"        <CdtrAcct>\n"
    f"            <Id>\n"
    f"                <IBAN>{beneficiaryAC}</IBAN>\n"
    f"            </Id>\n"
    f"        </CdtrAcct>\n"
    f"    </CdtTrfTxInf>\n"
    f" </FICdtTrf>\n"
    f"</Document>\n"
        
    )
    return pacs009_message
        

def search_20():
    # Retrieve values from input fields
    sender = field_sender.get()
    receiver = field_receiver.get()
    amount = field_amount.get()
    currency = field_currency.get()
    value_date = field_valuedate.get()
    reference = field_referencenumber.get()
    interemediary1 = field_intermediary1.get()
    interemediary2 = field_intermediary2.get()
    beneficiary = field_beneficiary.get()
    beneficiaryAC = field_beneficiaryAC.get()
    agent = field_agent.get()
    
    # Generate PACS 009 message
    pacs009_message = generate_pacs009(sender, receiver, amount, currency, value_date, reference,interemediary1, interemediary2, beneficiary, beneficiaryAC, agent)
    
    # Display PACS 009 message in output textbox
    PACS_output.configure(state="normal")
    PACS_output.delete("1.0", "end")
    PACS_output.insert("1.0", pacs009_message)
    PACS_output.configure(state="disabled")



window = customtkinter.CTk()
window.geometry("800x800")
window.title("MT202 to PACS Conversion")
window.resizable(False, False)

tabview = customtkinter.CTkTabview(master=window)
tabview.pack(pady=20, padx=60, fill="both", expand=True)

tab1 = tabview.add("INPUT MT202")
tab2 = tabview.add("OUTPUT PACS 009")

field_referencenumber = customtkinter.CTkLabel(master= tab1, text = "REFERENCE") 
field_referencenumber.grid(row=1, column=0, padx=10, pady=10)

field_referencenumber = customtkinter.CTkEntry(master = tab1)
field_referencenumber.grid(row=1, column=1, padx=10, pady=10)


field_rlatedreference = customtkinter.CTkLabel(master= tab1, text = "RELATED REFERENCE") 
field_rlatedreference.grid(row=2, column=0, padx=10, pady=10)

field_rlatedreference = customtkinter.CTkEntry(master = tab1)
field_rlatedreference.grid(row=2, column=1, padx=10, pady=10)

field_valuedate = customtkinter.CTkLabel(master= tab1, text = "Value date") 
field_valuedate.grid(row=3, column=0, padx=10, pady=10)

field_valuedate = customtkinter.CTkEntry(master = tab1, placeholder_text="XXXX-XX-XX")
field_valuedate.grid(row=3, column=1, padx=10, pady=10)


field_currency = customtkinter.CTkLabel(master= tab1, text = "CURRENCY") 
field_currency.grid(row=4, column=0, padx=10, pady=10)

currency = ["EUR", "CHF"]
field_currency = customtkinter.CTkComboBox(master = tab1, values= currency)
field_currency.grid(row=4, column=1, padx=10, pady=10)

field_amount = customtkinter.CTkLabel(master= tab1, text = "Amount") 
field_amount.grid(row=5, column=0, padx=10, pady=10)

field_amount = customtkinter.CTkEntry(master = tab1)
field_amount.grid(row=5, column=1, padx=10, pady=10)

field_intermediary1 = customtkinter.CTkLabel(master= tab1, text = "INTERMEDIARY 1") 
field_intermediary1.grid(row=6, column=0, padx=10, pady=10)

field_intermediary1 = customtkinter.CTkEntry(master = tab1)
field_intermediary1.grid(row=6, column=1, padx=10, pady=10)

field_intermediary2 = customtkinter.CTkLabel(master= tab1, text = "INTERMEDIARY 2") 
field_intermediary2.grid(row=7, column=0, padx=10, pady=10)

field_intermediary2 = customtkinter.CTkEntry(master = tab1)
field_intermediary2.grid(row=7, column=1, padx=10, pady=10)

field_agent = customtkinter.CTkLabel(master= tab1, text = "AGENT") 
field_agent.grid(row=8, column=0, padx=10, pady=10)

field_agent = customtkinter.CTkEntry(master = tab1)
field_agent.grid(row=8, column=1, padx=10, pady=10)

field_beneficiaryAC = customtkinter.CTkLabel(master= tab1, text = "BENEFICIARY ACCOUNT") 
field_beneficiaryAC.grid(row=9, column=0, padx=10, pady=10)

field_beneficiaryAC = customtkinter.CTkEntry(master = tab1)
field_beneficiaryAC.grid(row=9, column=1, padx=10, pady=10)

field_beneficiary = customtkinter.CTkLabel(master= tab1, text = "BENEFICIARY") 
field_beneficiary.grid(row=10, column=0, padx=10, pady=10)

field_beneficiary = customtkinter.CTkEntry(master = tab1)
field_beneficiary.grid(row=10, column=1, padx=10, pady=10)


field_sender = customtkinter.CTkLabel(master= tab1, text = "SENDER") 
field_sender.grid(row=0, column=0, padx=10, pady=10)

Sender = [""]
field_sender = customtkinter.CTkComboBox(master = tab1, values= Sender)
field_sender.grid(row=0, column=1, padx=10, pady=10)

field_receiver = customtkinter.CTkLabel(master= tab1, text = "RECEIVER") 
field_receiver.grid(row=0, column=3, padx=10, pady=10)

field_receiver = customtkinter.CTkEntry(master = tab1)
field_receiver.grid(row=0, column=4, padx=10, pady=10)

PACS_output = customtkinter.CTkTextbox(master=tab2, width=400, height=600)
PACS_output.pack(pady=12, padx=10)
PACS_output.configure(state="disabled")

search_button = customtkinter.CTkButton(master=window, text="GENERATE MX", command = search_20)
search_button.pack(pady=10)

window.mainloop()
