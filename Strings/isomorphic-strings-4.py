def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    mapping_st = {}
    mapping_ts = {}

    for cs, ct in zip(s, t):
        if mapping_st.get(cs, ct) != ct or mapping_ts.get(ct, cs) != cs:
            return False
        mapping_st[cs] = ct
        mapping_ts[ct] = cs

    return True
