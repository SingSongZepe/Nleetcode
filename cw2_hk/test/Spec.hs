{-# LANGUAGE TemplateHaskell #-}  
import Test.Hspec  
import Decimals (twoDecimalPlaces)

main :: IO ()  
main = hspec $ do  
   it "works for some examples" $ do
         twoDecimalPlaces 4.1537212 `shouldBe` 4.15
         twoDecimalPlaces 173735326.3783732637948948 `shouldBe` 173735326.38
       