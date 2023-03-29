from abc import ABC,abstractmethod
#Product Class
class Section(ABC):
    @abstractmethod
    def describe(self):
        pass
class PersonalSection(Section):
    def describe(self):
        print("Personal Section")
class AlbumSection(Section):
    def describe(self):
        print("Album Section")
class PatentSection(Section):
    def describe(self):
        print("Patent Section")
class PublicationSection(Section):
    def describe(self):
        print("Publication Section")

#Concrete Class 
class Profile(ABC):
    def __init__(self):
        self.sections=[]
        self.createProfile()
    @abstractmethod
    def createProfile(self):
        pass
    def getSections(self):
        return self.sections
    def addSections(self,section):
        self.sections.append(section)

#Concrete Class A
class linkedin(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(PatentSection())
        self.addSections(PublicationSection())

#Concrete Class B
class facebook(Profile):
    def createProfile(self):
        self.addSections(PersonalSection())
        self.addSections(AlbumSection())


if __name__=="__main__":
    profile_type=input("Which profile to create LINKEDIN or FACEBOOK")
    profile=eval(profile_type.lower())()
    print("Creating Profile",type(profile).__name__)
    print("Profile has sections",profile.getSections())
