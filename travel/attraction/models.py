from decimal import Decimal

from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

#from django.contrib.auth.models import User



# Create your models here.
class TouristAttraction(models.Model):
    name = models.CharField(max_length=100)
    #slug = models.SlugField(null=True)

    krabi = 'กระบี่'
    kanchanaburi = 'กาญจนบุรี'
    kalasin = 'กาฬสินธุ์'
    kamphaengPhet = 'กำแพงเพชร'
    khonKaen = 'ขอนแก่น'
    chanthaburi = 'จันทบุรี'
    chachoengsao = 'ฉะเชิงเทรา'
    chonburi = 'ชลบุรี'
    chainat = 'ชัยนาท'
    chaiyaphum = 'ชัยภูมิ'
    chumphon = 'ชุมพร'
    chiangMai = 'เชียงใหม่'
    chiangRai = 'เชียงราย'
    trang = 'ตรัง'
    trat = 'ตราด'
    tak = 'ตาก'
    nakhonNayok = 'นครนายก'
    nakhonPathom = 'นครปฐม'
    nakhonPhanom = 'นครพนม'
    nakhonRatchasima = 'นครราชสีมา'
    nakhonSiThammarat = 'นครศรีธรรมราช'
    nakhonSawan = 'นครสวรรค์'
    nonthaburi = 'นนทบุรี'
    narathiwat = 'นราธิวาส'
    nan = 'น่าน'
    buengKan = 'บึงกาฬ'
    buriram = 'บุรีรัมย์'
    pathumThani = 'ปทุมธานี'
    prachuapKhiriKhan = 'ประจวบคีรีขันธ์'
    prachinburi = 'ปราจีนบุรี'
    pattani = 'ปัตตานี'
    phraNakhonSiAyutthaya = 'พระนครศรีอยุธยา'
    phayao = 'พะเยา'
    phangNga = 'พังงา'
    phatthalung = 'พัทลุง'
    phichit = 'พิจิตร'
    phitsanulok = 'พิษณุโลก'
    phetchaburi = 'เพชรบุรี'
    phetchabun = 'เพชรบูรณ์'
    phrae = 'แพร่'
    phuket = 'ภูเก็ต'
    mahaSarakham = 'มหาสารคาม'
    mukdahan = 'มุกดาหาร'
    maeHongSon = 'แม่ฮ่องสอน'
    yasothon = 'ยโสธร'
    yala = 'ยะลา'
    roiEt = 'ร้อยเอ็ด'
    ranong = 'ระนอง'
    rayong = 'ระยอง'
    ratchaburi = 'ราชบุรี'
    lopburi = 'ลพบุรี'
    lampang = 'ลำปาง'
    lamphun = 'ลำพูน'
    loei = 'เลย'
    sisaket = 'ศรีสะเกษ'
    sakonNakhon = 'สกลนคร'
    songkhla = 'สงขลา'
    satun = 'สตูล'
    samutPrakan = 'สมุทรปราการ'
    samutSongkhram = 'สมุทรสงคราม'
    samutSakhon = 'สมุทรสาคร'
    saKaeo = 'สระแก้ว'
    saraburi = 'สระบุรี'
    singBuri = 'สิงห์บุรี'
    sukhothai = 'สุโขทัย'
    suphanBuri = 'สุพรรณบุรี'
    suratThani = 'สุราษฎร์ธานี'
    surin = 'สุรินทร์'
    nongKhai = 'หนองคาย'
    nongBuaLamphu = 'หนองบัวลำภู'
    angThong = 'อ่างทอง'
    amnatCharoen = 'อำนาจเจริญ'
    udonThani = 'อุดรธานี'
    uttaradit = 'อุตรดิตถ์'
    uthaiThani = 'อุทัยธานี'
    ubonRatchathani = 'อุบลราชธานี'
    bangkok = 'กรุงเทพ'

    PROVINCES = (
        (krabi, 'กระบี่'),
        (kanchanaburi, 'กาญจนบุรี'),
        (kalasin, 'กาฬสินธุ์'),
        (kamphaengPhet, 'กำแพงเพชร'),
        (khonKaen, 'ขอนแก่น'),
        (chanthaburi, 'จันทบุรี'),
        (chachoengsao, 'ฉะเชิงเทรา'),
        (chonburi, 'ชลบุรี'),
        (chainat, 'ชัยนาท'),
        (chaiyaphum, 'ชัยภูมิ'),
        (chumphon, 'ชุมพร'),
        (chiangMai, 'เชียงใหม่'),
        (chiangRai, 'เชียงราย'),
        (trang, 'ตรัง'),
        (trat, 'ตราด'),
        (tak, 'ตาก'),
        (nakhonNayok, 'นครนายก'),
        (nakhonPathom, 'นครปฐม'),
        (nakhonPhanom, 'นครพนม'),
        (nakhonRatchasima, 'นครราชสีมา'),
        (nakhonSiThammarat, 'นครศรีธรรมราช'),
        (nakhonSawan, 'นครสวรรค์'),
        (nonthaburi, 'นนทบุรี'),
        (narathiwat, 'นราธิวาส'),
        (nan, 'น่าน'),
        (buengKan, 'บึงกาฬ'),
        (buriram, 'บุรีรัมย์'),
        (pathumThani, 'ปทุมธานี'),
        (prachuapKhiriKhan, 'ประจวบคีรีขันธ์'),
        (prachinburi, 'ปราจีนบุรี'),
        (pattani, 'ปัตตานี'),
        (phraNakhonSiAyutthaya, 'พระนครศรีอยุธยา'),
        (phayao, 'พะเยา'),
        (phangNga, 'พังงา'),
        (phatthalung, 'พัทลุง'),
        (phichit, 'พิจิตร'),
        (phitsanulok, 'พิษณุโลก'),
        (phetchaburi, 'เพชรบุรี'),
        (phetchabun, 'เพชรบูรณ์'),
        (phrae, 'แพร่'),
        (phuket, 'ภูเก็ต'),
        (mahaSarakham, 'มหาสารคาม'),
        (mukdahan, 'มุกดาหาร'),
        (maeHongSon, 'แม่ฮ่องสอน'),
        (yasothon, 'ยโสธร'),
        (yala, 'ยะลา'),
        (roiEt, 'ร้อยเอ็ด'),
        (ranong, 'ระนอง'),
        (rayong, 'ระยอง'),
        (ratchaburi, 'ราชบุรี'),
        (lopburi, 'ลพบุรี'),
        (lampang, 'ลำปาง'),
        (lamphun, 'ลำพูน'),
        (loei, 'เลย'),
        (sisaket, 'ศรีสะเกษ'),
        (sakonNakhon, 'สกลนคร'),
        (songkhla, 'สงขลา'),
        (satun, 'สตูล'),
        (samutPrakan, 'สมุทรปราการ'),
        (samutSongkhram, 'สมุทรสงคราม'),
        (samutSakhon, 'สมุทรสาคร'),
        (saKaeo, 'สระแก้ว'),
        (saraburi, 'สระบุรี'),
        (singBuri, 'สิงห์บุรี'),
        (sukhothai, 'สุโขทัย'),
        (suphanBuri, 'สุพรรณบุรี'),
        (suratThani, 'สุราษฎร์ธานี'),
        (surin, 'สุรินทร์'),
        (nongKhai, 'หนองคาย'),
        (nongBuaLamphu, 'หนองบัวลำภู'),
        (angThong, 'อ่างทอง'),
        (amnatCharoen, 'อำนาจเจริญ'),
        (udonThani, 'อุดรธานี'),
        (uttaradit, 'อุตรดิตถ์'),
        (uthaiThani, 'อุทัยธานี'),
        (ubonRatchathani, 'อุบลราชธานี'),
        (bangkok, 'กรุงเทพมหานคร')
    )
    province = models.CharField(max_length=50, choices=PROVINCES, default=bangkok)

    temple = 'วัด'
    sea = 'ทะเลและชายหาด'
    royalProject = 'โครงการหลวงและโครงการในพระราชดำริ'
    waterfall = 'น้ำตก'
    recreation = 'สันทนาการและกีฬา'
    wildlife = 'ธรรมชาติและสัตว์ป่า'
    heritage = 'ศิลปะ วัฒนธรรม แหล่งมรดก และสถาปัตยกรรม'
    religiousPlace = 'สถานที่เกี่ยวกับศาสนาอื่นๆ'
    museum = 'พิพิธภัณฑ์'
    locality = 'เที่ยวท้องถิ่น'
    technical = 'สถานที่ท่องเที่ยวเชิงวิชาการ'
    another = 'อื่นๆ'
    palace = 'พระราชวัง'
    shopping = 'ชอปปิง'
    vineyard = 'ไร่องุ่นและโรงงานเบียร์'
    spa = 'สปาเพื่อสุขภาพ'
    TYPES = (
        (temple, 'วัด'),
        (sea, 'ทะเลและชายหาด'),
        (royalProject, 'โครงการหลวงและโครงการในพระราชดำริ'),
        (waterfall, 'น้ำตก'),
        (recreation, 'สันทนาการและกีฬา'),
        (wildlife, 'ธรรมชาติและสัตว์ป่า'),
        (heritage, 'ศิลปะ วัฒนธรรม แหล่งมรดก และสถาปัตยกรรม'),
        (religiousPlace, 'สถานที่เกี่ยวกับศาสนาอื่นๆ'),
        (museum, 'พิพิธภัณฑ์'),
        (locality, 'เที่ยวท้องถิ่น'),
        (technical, 'สถานที่ท่องเที่ยวเชิงวิชาการ'),
        (palace, 'พระราชวัง'),
        (another, 'อื่นๆ'),
        (shopping, 'ชอปปิง'),
        (vineyard, 'ไร่องุ่นและโรงงานเบียร์'),
        (spa, 'สปาเพื่อสุขภาพ'),
    )
    kindOf = models.CharField(max_length=100, choices=TYPES, default=another)
    contact = models.CharField(max_length=100, blank=True, null=True)
    time = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    img = models.URLField(blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=Decimal('0.000000'))
    lng = models.DecimalField(max_digits=9, decimal_places=6, default=Decimal('0.000000'))

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def no_of_ratings(self):
        ratings = Rating.objects.filter(touristtttraction=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(touristtttraction=self)
        for rating in ratings:
            sum += rating.stars

        if len(ratings) > 0:
            return sum/len(ratings)
        else:
            return 0

class Rating(models.Model):
    touristattraction = models.ForeignKey(TouristAttraction, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'touristattraction'),)
        index_together = (('user', 'touristattraction'),)




class Rank(models.Model):
    rank_number = models.IntegerField()
    rank_province = 'ระดับจังหวัด'
    rank_country = 'ระดับประเทศ'
    TYPE2 = (
        (rank_province, 'ระดับจังหวัด'),
        (rank_country, 'ระดับประเทศ')
    )
    rank_type = models.CharField(max_length=100, choices=TYPE2, default=rank_country)
    touristattraction = models.ForeignKey(TouristAttraction, on_delete=models.CASCADE)

    def __str__(self):
        return self.rank_type
