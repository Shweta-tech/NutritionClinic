from django import forms
from .models import breastfeed,childreg,immunizatn

class breastfeeding(forms.ModelForm):
    wash = forms.CharField()
    water = forms.CharField()
    sat = forms.CharField()
    back = forms.CharField()
    shldr = forms.CharField()
    uncvrd = forms.CharField()
    pressure = forms.CharField()
    unwrapped = forms.CharField()
    heldbaby = forms.CharField()
    legstucked = forms.CharField()
    elevatebaby = forms.CharField()
    thumb = forms.CharField()
    wrist = forms.CharField()
    babytummy = forms.CharField()
    head = forms.CharField()
    nose = forms.CharField()
    fullbody = forms.CharField()
    chin = forms.CharField()
    cupped = forms.CharField()
    finger = forms.CharField()
    distance = forms.CharField()
    parallel = forms.CharField()
    compressbaby = forms.CharField()
    equal = forms.CharField()
    avoid = forms.CharField()
    open = forms.CharField()
    mouth = forms.CharField()
    upperlips = forms.CharField()
    lowerlip = forms.CharField()
    latched = forms.CharField()
    chins = forms.CharField()
    lower = forms.CharField()
    fedfrombreast = forms.CharField()
    empty = forms.CharField()
    foremilk = forms.CharField()
    offer = forms.CharField()
    burped = forms.CharField()
    wokeup = forms.CharField()
    used = forms.CharField()
    hunger = forms.CharField()
    nosepressed = forms.CharField()
    latching = forms.CharField()
    brestfeedhrs = forms.CharField()
    bfnyt = forms.CharField()
    growth = forms.CharField()

    class Meta:
        model = breastfeed
        fields = ('wash','water','sat','back','shldr','uncvrd','pressure','unwrapped','heldbaby','legstucked','elevatebaby','thumb','wrist','babytummy','head','nose','fullbody','chin','cupped','finger','distance','parallel','compressbaby','equal','avoid','open','mouth','upperlips','lowerlip','latched','chins','lower','fedfrombreast','empty','foremilk','offer','burped','wokeup','used','hunger','nosepressed','latching','brestfeedhrs','bfnyt','growth')


class childregister(forms.ModelForm):
    date_of_reg = forms.DateField()
    child_id = forms.IntegerField() 
    child_name = forms.CharField()
    cimage =forms.ImageField()
    birth_date = forms.CharField()
    age = forms.IntegerField()
    age_in_months = forms.IntegerField()
    age_in_days = forms.IntegerField()
    gender = forms.CharField()
    mother_name = forms.CharField()
    mother_s_age = forms.IntegerField()
    mother_height = forms.DecimalField() 
    mcontact_no = forms.IntegerField()
    father_height = forms.DecimalField() 
    fcontact_no = forms.IntegerField()
    address_geolocate = forms.CharField()
    no_of_siblings = forms.IntegerField()
    nmbrbrthrs = forms.CharField()
    nmbrsis = forms.CharField()
    num_deaths_sblngs = forms.CharField()
    cause_deaths_sblngs = forms.CharField()
    dob_last_child = forms.CharField()
    religion = forms.CharField()
    name_of_gynecologist = forms.CharField()
    name_of_pediatrician = forms.CharField()
    institution = forms.CharField()
    specifyothrs = forms.CharField()
    presenceatdelivery = forms.CharField()
    type = forms.CharField()
    gestational = forms.CharField()
    birth_weight = forms.DecimalField() 
    birth_length_in_cms = forms.DecimalField() 
    discharge_weight = forms.DecimalField() 
    conditionatbirth = forms.CharField()
    babytransfertotherhsptl = forms.CharField()
    specifycause = forms.CharField()
    breastcrawlimmediatedone = forms.CharField()
    bfdone = forms.CharField()
    umbilicalcut = forms.CharField()
    vitamink = forms.CharField()
    antenalvisit = forms.CharField()
    breastfeedskill = forms.CharField()
    bywhom = forms.CharField()
    othersspecify = forms.CharField()
    holdduringbreastfeed = forms.CharField()
    onlybrstmilk = forms.CharField()
    besidemilk = forms.CharField()
    whatanythin = forms.CharField()
    anythingspecify = forms.CharField()
    dctrprscribtn = forms.CharField()
    specifyanyone = forms.CharField()
    conditionofmother = forms.CharField()
    kangaroocare = forms.CharField()
    skintouchforhr = forms.CharField()
    specify9_name = forms.CharField()
    babybath = forms.CharField()
    babyvaccine = forms.CharField()
    whichvaccine = forms.CharField()
    breastfeedathome = forms.CharField()
    specifyplace = forms.CharField()
    baseline_weight = forms.DecimalField()
    weight_percentile = forms.DecimalField() 
    baseline_height = forms.DecimalField() 
    length_height_percentile = forms.DecimalField() 
    head_circumference_cm = forms.DecimalField() 
    baseline_muac_mm = forms.DecimalField() 
    baseline_stntd_stats = forms.CharField()
    baseline_uw_status = forms.CharField()
    baseline_wstng_stats = forms.CharField()

    class Meta:
        model = childreg
        fields = ('date_of_reg', 'child_id', 'child_name','cimage','birth_date','age', 'age_in_months','age_in_days', 'gender','mother_name','mother_s_age' ,'mother_height' ,'mcontact_no' ,'father_height','fcontact_no' ,'address_geolocate' ,'no_of_siblings' ,'nmbrbrthrs','nmbrsis','num_deaths_sblngs' ,'cause_deaths_sblngs','dob_last_child' ,'name_of_gynecologist' ,'name_of_pediatrician','institution','specifyothrs' ,'presenceatdelivery' ,'type' ,'gestational' ,'birth_weight' ,'birth_length_in_cms','religion','discharge_weight','conditionatbirth','babytransfertotherhsptl','specifycause','breastcrawlimmediatedone','bfdone' ,'umbilicalcut','vitamink','antenalvisit' ,'breastfeedskill' ,'bywhom','othersspecify' ,'holdduringbreastfeed' ,'onlybrstmilk','besidemilk' ,'whatanythin' ,'anythingspecify','dctrprscribtn' ,'specifyanyone','conditionofmother','kangaroocare' ,'skintouchforhr','specify9_name','babybath' ,'babyvaccine','whichvaccine','breastfeedathome','specifyplace','baseline_weight','weight_percentile','baseline_height','length_height_percentile','head_circumference_cm' ,'baseline_muac_mm' ,'baseline_stntd_stats' ,'baseline_uw_status','baseline_wstng_stats')


class immniztn(forms.ModelForm):
    cid = forms.CharField()
    cname = forms.CharField()
    measles = forms.CharField()
    optradio = forms.CharField()
    bcg = forms.CharField()
    hb = forms.CharField()
    opv = forms.CharField()
    opvweeks = forms.CharField()
    msls = forms.CharField()
    opvten = forms.CharField()
    rota = forms.CharField()
    vitmin = forms.CharField()
    rvirs = forms.CharField()
    opvforteen = forms.CharField()
    ipv = forms.CharField()
    mesls = forms.CharField()
    ipvweeks = forms.CharField()
    vitaminfiv = forms.CharField()
    pen = forms.CharField()
    opvboost = forms.CharField()
    thrdose = forms.CharField()
    dpt = forms.CharField()
    vitmina = forms.CharField()
    vitminafr = forms.CharField()
    vitminae8 = forms.CharField()
    pentav = forms.CharField()
    vitamina2 = forms.CharField()
    vitamina6 = forms.CharField()
    pen14 = forms.CharField()
    rota10 = forms.CharField()
    vitamin7 = forms.CharField()


    class Meta:
        model = immunizatn
        fields = ('cid','cname','measles','optradio','bcg','hb','opv','opvweeks','msls','opvten','rota','vitmin','rvirs','opvforteen','ipv','mesls','ipvweeks','vitaminfiv','pen','opvboost','thrdose','dpt','vitmina','vitminafr','vitminae8','pentav','vitamina2','vitamina6','pen14','rota10','vitamin7')
