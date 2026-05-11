class Solution:
    def checkValidString(self, s: str) -> bool:
        st = []
        star = []
        for idx, char in enumerate(s):
            if char == "(":
                st.append(idx)
            elif char == "*":
                star.append(idx)
            else:
                if st:
                    st.pop()
                elif  star:
                    star.pop()
                else:
                    return False
        
        while st and star:
            if st[-1] > star[-1]:
                return False
            st.pop()
            star.pop()
        return not st