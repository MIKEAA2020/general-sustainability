"""Serialize finite mpmath interval endpoints as outward decimal bounds.
Uses exact integer arithmetic on the underlying binary mpf tuples; ordinary
nearest-rounded decimal formatting is not used for interval endpoints.
"""
def _decimal_endpoint(binary,places,upper):
    sign,man,exponent,_=binary
    numerator=(-man if sign else man)
    denominator=1
    if exponent>=0:numerator<<=exponent
    else:denominator<<=-exponent
    scaled=numerator*10**places
    integer=-((-scaled)//denominator)if upper else scaled//denominator
    negative=integer<0;digits=str(abs(integer)).zfill(places+1)
    return ('-'if negative else'')+digits[:-places]+'.'+digits[-places:]

def outward_bounds(interval,places=60):
    if places<1:raise ValueError('places must be positive')
    return [_decimal_endpoint(interval._mpi_[0],places,False),_decimal_endpoint(interval._mpi_[1],places,True)]
