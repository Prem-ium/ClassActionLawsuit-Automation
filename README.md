<h1 align="center"> 📝 Class Action AutoFill 💼 </h1>
<p align="center">Quick, easy class action form automation.</p>

<p align="right">
    <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
    <img src="https://img.shields.io/badge/-selenium-%43B02A?style=for-the-badge&logo=selenium&logoColor=white"/>
    <a href="https://github.com/sponsors/Prem-ium" target="_blank">
        <img src="https://img.shields.io/badge/sponsor-30363D?style=for-the-badge&logo=GitHub-Sponsors&logoColor=#EA4AA" alt="Github Sponsor"/>
    </a>
</p>

---

## 🔍 Overview 

The **Class Action AutoFill** tool is an **experimental automation script** designed to streamline the process of completing class action lawsuit claim forms. Currently, it supports one specific landing page, with future updates planned to expand functionality.

---

## 🛠 Features

- **Automates Form Completion**: Quickly fill out personal details on class action forms.  
- **Supports Multiple Users**: Handles claims for multiple individuals from a single configuration file.  
- **Python-Powered**: Built with Python and Selenium WebDriver for robust automation.  
- **Environment Variable Configuration**: Uses a `.env` file to securely manage user data.

---
## 🎥 Demo  

The following is a brief demonstration of the tool’s capabilities. Please note that this is an **outdated demo**, and an updated version is coming soon!  

<video src="https://github.com/user-attachments/assets/a4ef3f49-df59-44fb-9ef0-16190991dcd0" controls="controls" style="max-width: 100%; height: auto;">
  Your browser does not support video tags.
</video>

---
## 🌟 Exclusive for Sponsors  

This project is available exclusively to **Gold Sponsors** on GitHub ($10/month). By sponsoring, you'll gain:  

- Access to the private repository containing the full script and documentation.  
- Regular updates with additional landing page support and new features.  
- A direct line to provide feedback and suggestions.  

[💛 Become a Gold Sponsor](https://github.com/sponsors/Prem-ium)  

---

## ⚙️ Environment Variables  

The tool leverages a `.env` file for configuration. Below are examples of the variables you’ll need:  

### Example `.env` File  
```bash
PEOPLE='[
    {"FirstName":"Alex","LastName":"Nas","Address":"123 Fake Street","City":"Atlanta","State":"Georgia","Country":"United States","Zip":"31083","Phone":"9083756473","Email":"alex-nas@gmail.com"},
    {"FirstName":"Jane","LastName":"Doe","Address":"456 Real Street","City":"New York","State":"New York","Country":"USA","Zip":"10001","Phone":"1234567890","Email":"jane-doe@gmail.com"}
]'
```
### Key Fields  

- **`FirstName`**: First name of the claimant.  
- **`LastName`**: Last name of the claimant.  
- **`Address`**, **`City`**, **`State`**, **`Country`**, **`Zip`**: Full address details.  
- **`Phone`**, **`Email`**: Contact information.  

---

## 🚀 Instructions  

For setup and detailed usage instructions, please refer to the [private sponsor repository's README](https://github.com/PremiumSponsor/sponsors/blob/main/Auto-ClassAction/README.md).

---

## 🛡️ Disclaimer  

- **Perjury Warning**: Submitting false claims for class action lawsuits may constitute **perjury**, a serious criminal offense. Ensure you meet all eligibility requirements before using this tool to file any claims. Misuse of this tool for ineligible claims may result in legal consequences.  

- **User Responsibility**: You are solely responsible for the accuracy and legality of all information submitted using this tool. The developer has no way to verify the validity of your claims and provides no guarantees of compliance with legal or procedural requirements.  

- **Developer Liability Waiver**: The developer is not liable for any misuse, abuse, or neglect related to the use of this tool. This includes, but is not limited to, account restrictions, denial of claims, or legal repercussions arising from improper use. By using this tool, you agree to accept full responsibility for your actions and release the developer from any claims of liability.  

- **Mistaken Claims**: If you unintentionally file a claim for which you are not eligible, it is your duty to contact the relevant authorities (typically listed on the lawsuit’s website) to withdraw or correct the claim. Failure to do so may lead to penalties or rejection of future claims.  

**Use this tool responsibly and ensure all claims align with the guidelines outlined in the class action lawsuit's terms and conditions.**  
