from app import helper


def transformGeo(geometry,toCRS):
    return 'st_transform(st_geomfromtext(\''+ str(geometry) +'\'::text,4326),' + str(toCRS) + ')'

def get_exists_table_query(tbname, schema):
    return """ SELECT EXISTS (
                        SELECT 1
                        FROM   information_schema.tables 
                        WHERE  table_schema = '""" + schema + """'
                        AND    table_name = '""" + tbname + """'
                    );"""

def vector_query(scalevalue,vector_table_requested, geometry,toCRS):
    """
    this function will return the need scale query select the scalevalue
    :param scalevalue:
    :param vector_table_requested:
    :param geometry:
    :param toCRS:
    :return: the right query select the scalevalue
    """
    if scalevalue == 'hectare':
        return vector_query_hectares(vector_table_requested, geometry,toCRS)
    elif scalevalue == 'nuts':
        id_selected_list = helper.adapt_nuts_list(geometry)
        return vector_query_nuts(vector_table_requested, id_selected_list)
    elif scalevalue == 'lau':
        id_selected_list = helper.adapt_nuts_list(geometry)
        return vector_query_lau(vector_table_requested, id_selected_list,toCRS)
    return None



def vector_query_hectares(vector_table_requested, geometry,toCRS):
    """
    this function will return an array of the vector table selected at hectares
    :param vector_table_requested:
    :param geometry:
    :param toCRS:
    :return:
    """

    query= 'with subAreas as ( SELECT nuts.nuts_id,nuts.gid FROM geo.nuts ' + \
           'where ST_Intersects( nuts.geom,' + \
           ' '+transformGeo(geometry,toCRS)+' ) '  + \
           "AND STAT_LEVL_ = 0 AND year = to_date('2013', 'YYYY') ) " + \
           'select * from stat.' + vector_table_requested + ',subAreas ' + \
           'where fk_nuts_gid = subAreas.gid'
    print ('query ',query)

    return query

def vector_query_nuts(vector_table_requested, area_selected):
    """
    this function will return an array of the vector table selected from a selection at hectare level
    :param vector_table_requested:
    :param geometry:
    :return:
    """
    vector_table_requested = str(vector_table_requested)
    query= 'with selected_zone as ( SELECT geom as geom from geo.nuts where nuts_id IN('+ area_selected+') ' \
                                                                                                        "AND year = to_date('2013', 'YYYY') ), subAreas as ( SELECT distinct geo.nuts.nuts_id,geo.nuts.gid " \
                                                                                                        'FROM selected_zone, geo.nuts where ST_Intersects( geo.nuts.geom, selected_zone.geom ) ' \
                                                                                                        "AND geo.nuts.STAT_LEVL_ = 0 AND geo.nuts.year = to_date('2013', 'YYYY') ) " \
                                                                                                        'select * from stat.' + vector_table_requested + ',subAreas where fk_nuts_gid = subAreas.gid'

    return query


def vector_query_lau(vector_table_requested, area_selected,toCRS):
    """
    this function will return an array of the vector table selected from a selection at lau level
    :param vector_table_requested:
    :param geometry:
    :return
    """

    query= 'with selected_zone as ( SELECT geom' \
                                                       ' from public.tbl_lau1_2 where comm_id IN('+ area_selected+')  ),' \
                                                                                                        ' subAreas as ( SELECT distinct geo.nuts.nuts_id, geo.nuts.gid FROM selected_zone, geo.nuts ' \
                                                                                                        'where ST_Intersects( geo.nuts.geom, selected_zone.geom ) AND geo.nuts.STAT_LEVL_ = 0 ' \
                                                                                                        "AND geo.nuts.year = to_date('2013', 'YYYY') ) select * from stat." + vector_table_requested + ',subAreas where fk_nuts_gid = subAreas.gid'

    return query


def nuts_within_the_selection(geometry,toCRS):
    query= 'SELECT nuts.nuts_id FROM geo.nuts ' + \
           'where ST_Intersects( nuts.geom,' + \
           ' '+transformGeo(geometry,toCRS)+" ) AND geo.nuts.STAT_LEVL_ = 2 AND year = to_date('2013', 'YYYY')"
    print ('query ',query)

    return query
def nuts2_within_the_selection_nuts_lau(scalevalue, geometry,toCRS):
    """
    this function will return the need scale query select the scalevalue
    :param scalevalue:
    :param vector_table_requested:
    :param geometry:
    :param toCRS:
    :return: the right query select the scalevalue
    """

    if scalevalue == 'nuts':
        id_selected_list = helper.adapt_nuts_list(geometry)
        return nuts2_within_the_selection_nuts(id_selected_list,toCRS)
    elif scalevalue == 'lau':
        id_selected_list = helper.adapt_nuts_list(geometry)
        return nuts2_within_the_selection_lau(id_selected_list,toCRS)
    return None

def nuts2_within_the_selection_nuts(area_selected,toCRS):
    query= 'with selected_zone as ( SELECT geom as geom from geo.nuts where nuts_id IN('+ area_selected+') ' \
                                                                                                        "AND year = to_date('2013', 'YYYY') ), subAreas as ( SELECT distinct geo.nuts.nuts_id,geo.nuts.gid " \
                                                                                                        'FROM selected_zone, geo.nuts where ST_Intersects( geo.nuts.geom, selected_zone.geom ) ' \
                                                                                                        "AND geo.nuts.STAT_LEVL_ = 2 AND geo.nuts.year = to_date('2013', 'YYYY') ) " \
                                                                                                        'select subAreas.nuts_id from subAreas'
    return query




def nuts2_within_the_selection_lau(area_selected,toCRS):
    query= 'with selected_zone as ( SELECT geom' \
           ' from public.tbl_lau1_2 where comm_id IN('+ area_selected+')  ),' \
                                                                      ' subAreas as ( SELECT distinct geo.nuts.nuts_id, geo.nuts.gid FROM selected_zone, geo.nuts ' \
                                                                      'where ST_Intersects( geo.nuts.geom, selected_zone.geom ) AND geo.nuts.STAT_LEVL_ = 2 ' \
                                                                      "AND geo.nuts.year = to_date('2013', 'YYYY') ) select subAreas.nuts_id from subAreas"
    print ('query', query)
    return query

