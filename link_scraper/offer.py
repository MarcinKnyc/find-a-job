from datetime import datetime
from typing import Optional

def cast_pracuj_str_to_datetime(str_datetime: str) -> datetime:
    """
    Pracuj.pl saves dates in format like: 2023-11-08T22:59:59ZZ
    We cast this to python datetime to avoid confusion.
    """
    return datetime.strptime(str_datetime[:-2], '%Y-%m-%dT%H:%M:%S')


class Offer:
    def __init__(
            self,
            title: str, 
            hiringOrganization: str, 
            datePosted: str, #argument is str, field in class is datetime
            validThrough: str, #argument is str, field in class is datetime
            addressCountry: str,
            addressRegion: str,
            addressLocality: str,
            postalCode: Optional[str],
            streetAddress: Optional[str],
            employmentType: str,
            industry: str,
            baseSalary: Optional[float],
            jobBenefits: Optional[str],
            responsibilities: str,
            experienceRequirements: str,
            link_id: int
        ):
        self.title = title
        self.hiringOrganization = hiringOrganization
        self.datePosted = cast_pracuj_str_to_datetime(datePosted)
        self.validThrough = cast_pracuj_str_to_datetime(validThrough)
        self.addressCountry = addressCountry
        self.addressRegion = addressRegion
        self.addressLocality = addressLocality
        self.postalCode = postalCode
        self.streetAddress = streetAddress
        self.employmentType = employmentType
        self.industry = industry
        self.baseSalary = baseSalary
        self.jobBenefits = jobBenefits
        self.responsibilities = responsibilities
        self.experienceRequirements = experienceRequirements
        self.link_id = link_id
        
