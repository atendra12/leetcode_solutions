class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        for email in emails:
            unique_emails.add(email.split('@')[0].replace('.','').split('+')[0] + '@'+email.split('@')[1])
        
        return len(unique_emails)

        