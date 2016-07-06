"""Populate the item catalog database some initial content.

This application stores scientific papers  of various subjects. Five  categories are
created and some of my favorite publications have been added in each category.

This script should only be run on an empty database.
"""
from sqlalchemy import func

from catalog.database_setup import User, Category, Item
from catalog.connect_to_database import connect_to_database

def populate_database():
    """Populate the item catalog database some initial content."""
    session = connect_to_database()

    # Make sure the database is empty before running this inital data dump.
    category_count = session.query(func.count(Category.id)).scalar()
    if category_count > 0:
        session.close()
        return

    
    category1 = Category(name="Civ Eng")
    session.add(category1)
    session.commit()

    category2 = Category(name="Physics")
    session.add(category2)
    session.commit()

    category3 = Category(name="Maths")
    session.add(category3)
    session.commit()

    category4 = Category(name="Bioinformatics")
    session.add(category4)
    session.commit()

    category5 = Category(name="Comp Sci")
    session.add(category5)
    session.commit()

    #category6 = Category(name="A-Level Chem")
   # session.add(category6)
   # session.commit()

    #category7 = Category(name="Soundcloud")
    #session.add(category7)
   # session.commit()


    
    user1 = User(name="tony1", email="tb@science.com")
    session.add(user1)
    session.commit()

    
    item1 = Item(
        user=user1,
        category=category2,
        name="Violation of Bell Inequality",
        description=(
            "This marks the first time a loop free violation of Bell's inequality has been experimentally achieved. This means the property of entanglement between quantum particles (In this case photon pairs) has been experimentally verified with both loopholes closed. In my opinion entanglement is a misleading word to describe this property. For a specific set of experimental conditions the photon pairs are correlated in way that cannot be measured  using classical physics. [Right click on above pdf image to download full paper]"
            ),
        quantity=1,
        image_url="http://arxiv.org/pdf/1511.03189v1.pdf"
    )
    session.add(item1)
    session.commit()

    item2 = Item(
        user=user1,
        category=category2,
        name="The definitive reason for wave-particle duality",
        description=(
            "This is a work of brilliance. Here for the first time it is shown why that double slit experiment produces wave properties from single particles. It is in fact a direct consequence of the Heisenberg uncertainty principle. In fact Feynman's Lectures Volume 3 almost arrives at this conclusion in it's first chapter. So much so I susupected for many years that wave-particle duality was a manifestation of the uncertainty principle. [Right click on above pdf image to download full paper]"
        ),
        quantity=1,
        image_url="http://arxiv.org/pdf/1403.4687v2.pdf"

    )
    session.add(item2)
    session.commit()

    
    item3 = Item(
        user=user1,
        category=category1,
        name="Why Did the World Trade Center Collapse? Simple Analysis",
        description=(
            "This is a great paper. Short yet  succinct. The authors clearly show how the WTC 1 and 2 collapsed due to the damage caused by the plane impact. I just to want to point out here also that many people have gotten the idea that the plane impact could not have collapsed the towers in the way that they did (straight down) citing simliarities to controlled demolition collapse. This simply is not true. It is entirely possible for buildings to collapse in this way from different mechanisms of structural damage. This paper outlines the way in which this happened for the collapse of the World Trade Towers. [Right click on above pdf image to download full paper]"
        ),
        quantity=1,
        image_url="http://www.civil.northwestern.edu/people/bazant/PDFs/Papers/405.pdf"
    )
    session.add(item3)
    session.commit()

    item4 = Item(
        user=user1,
        category=category3,
        name="The Math in 'Good Will Hunting'",
        description=(
            "This is a lovely paper. The authors go through the thinking behind the Math probelems that Matt Damon solves in Good Will Hunting. The first one is quite tricky. An enjoyable read if like me you were wondering what Matt Damon's character was writing about. [Right click on above pdf image to download full paper]"
            
        ),
        quantity=1,
        image_url="http://mat.unideb.hu/media/horvath-gabor/publications/gwh2.pdf"
    )
    session.add(item4)
    session.commit()

   
    item5 = Item(
        user=user1,
        category=category3,
        name="RSA Crpytography",
        description=(
            "This was the first real world application of number theory to technology. Some mathematicians and computer scientists figured out they could use modular arithmitic and prime factorization to encode messages using a  public key and private key methodology. [Right click on the above pdf image to download full paper]"
            
            
            
        ),
        quantity=1,
        image_url="http://people.csail.mit.edu/rivest/Rsapaper.pdf"
    )
    session.add(item5)
    session.commit()

    item6 = Item(
        user=user1,
        category=category4,
        name="Bioconductor",
        description=(
            "Bioconductor is such a powerful platform. Whenever you want to carry out gene expression analysis and or even more general biostatistics applications bioconductor has a package you can download and use with the statistics langauge R. It's like linux for biology folk. Not too much support in the assembling genomes area unfortunately. But there's a great interface called R Studio that works beautifully with bioconductor packages. [Right click on the above pdf image to download full paper]"
            ),
        quantity=1,
        image_url="http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4509590/pdf/nihms-661499.pdf"
    )
    session.add(item6)
    session.commit()

    
   # item7 = Item(
       # user=user1,
       # category=category4,
       # name="Velvet",
        #description=(
           # "This was the first type of genome assembler to apply the concept  an Eulerian path"
          # " through a DeBrujin graph as the algorthim to assemble contigs. Quite a remarkable package."
#"You need to carefully pick what kmer size to use however and also a value for coverage."
#" There is another package bundled with velvet called velvet optimiser that can optimise the choice of parameters. "
           # ),
        #quantity=2,
       # image_url="http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2336801/pdf/821.pdf"
   # session.add(item7)
   # session.commit()

    item8 = Item(
        user=user1,
        category=category5,
        name="PageRank",
        description=(
            "The world changed (for the better in my opinion) when Larry and Sergei hit upon the idea of replacing matrix rows whose entries were zeros  with 1/n. The matrix of course was the one that kept track of all webpages. This matrix changed a vector of incoming links to out going links. The zero rows correspond to pages with no outgoing links. Like the link to the pdf you are about to right click on. :D "
           
            
           
          
        ),
        quantity=1,
        image_url="http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf"
    )
    session.add(item8)
    session.commit()

    
    item9 = Item(
        user=user1,
        category=category5,
        name="AKS Primality Test",
        description=(
            "During the first week of my degree in Math and Physics back in Sep 2003 there was a Math Soc Talk advertised about primality testing. This is a big problem in number theory. How to detrmine if a number is prime or not. Up until 2002 the main methods were very slow. AKS is the first primality-proving algorithm to be simultaneously general, polynomial, deterministic, and unconditional. This was huge! And it had just happened! I recommend reading the wiki for this one also. Two of the Three authors were actually students at the time also! [Right click on above pdf image to download full paper]"
            
            
            
            
            
        ),
        quantity=1,
        image_url="http://www.cse.iitk.ac.in/users/manindra/algebra/primality_v6.pdf"
    )
    session.add(item9)
    session.commit()

    item10 = Item(
        user=user1,
        category=category4,
        name="Velvet",
        description=(
            "This was the first type of genome assembler to apply the concept of  an Eulerian path through a DeBrujin graph as the algorthim to assemble contigs. Quite a remarkable package. You need to carefully pick what kmer size to use however and also a value for coverage. There is another package bundled with velvet called velvet optimiser that can optimise the choice of parameters. [Right click on above pdf image to download full paper] "
            
            
           
            
            
            
        ),
        quantity=1,
        image_url="http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2336801/pdf/821.pdf"
    )
    session.add(item10)
    session.commit()

    print "Populated database with some papers..."


if __name__ == '__main__':
    populate_database()
