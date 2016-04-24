# don't overthink this problem either...

input="unknowndigits"

def password_decrypter(password):
    changed=changer(password)
    weird=weirder(changed)
def changer(q):
    altered_password=""
    for c in q: altered_password+=chr(ord(c)*2)
    return altered_password
def weirder(l):
    o=""
    cu=-1
    c=[98,101,103,120,100,97,133,103,109,89,105,101,98,202,123]
    for h in l:
        cu+=1
        o+=chr((ord(h)-c[cu]))
    return(o)
def newFunction():
    p="Bacon ipsum dolor amet proident short loin ut pariatur consectetur t-bone cupidatat aliqua et fatback filet mignon ham prosciutto leberkas. Non ut beef ribs doner consectetur ea id pork loin fatback spare ribs kielbasa cillum ball tip. Duis andouille pancetta, anim adipisicing turducken chicken tri-tip t-bone.{ Officia prosciutto minim, aliquip esse ullamco ut do dolore sausage jerky quis ham hock ground round elit. Exercitation bacon ex pastrami, dolor short loin aute. Pastrami ground round enim aliqua, anim capicola officia elit spare ribs swine strip steak ullamco sed labore. Swine porchetta ad aliqua. Rump in aute tri-tip, pork belly id pork loin et frankfurter dolore ullamco ut tail lorem. Labore salami aute esse shankle jowl tempor mollit ground round venison fugiat enim elit chuck eu. Ham hock shank elit aliqua. Sausage alcatra ullamco brisket dolore minim tempor biltong ut qui sunt aliqua swine nisi chicken. Andouille shankle porchetta rump tempor doner. Chuck brisket short loin nisi. Dolor in lflank eu duis ham fatback.Rump in jerky landjaeger tail eiusmod enim swine velit non brisket. Kielbasa laboris veniam, mollit aute frankfurter andouille. Landjaeger in beef ribs tongue short loin in eiusmod porchetta filet mignon magna irure aliqua. Leberkas reprehenderit pig shoulder fiet mignon laborum porchetta bacon strip steak qui et ut alcatra dolor sirloin. Jowl doner spare ribs porchetta dolore elit et turkey in salami.Adipisicing ex turducken magna. Ex strip steak sausage short ribs cupim. Deserunt proident occaecat, frankfurter swine in aliqua andouille ut tri-tip ex eiusmod bacon. }Labore pancetta tenderloin duis sint laboris ea tri-tip pork fugiat. Andouille sint rump, sed officia landjaeger boudin sirloin mollit ullamco capicola enim. Boudin beef ribs chicken, fugiat pig lorem doner labore chuck pork chop_excepteur pican"
    return (p[115]+p[166]+p[1793]+p[67]+p[776]+p[311]+p[1388]+p[160]+p[1220]+p[1454]+p[1847]+p[1024]+p[1611]+p[548]+p[1056]+p[1617])

password_decrypter(input)