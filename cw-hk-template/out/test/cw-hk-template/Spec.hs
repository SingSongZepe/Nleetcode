{-# LANGUAGE TemplateHaskell #-}  
import Test.Hspec  
import RenameMe (renameMe)  

main :: IO ()  
main = hspec $ do  
    describe "square" $ do  
        it "calculates the square of a number" $ do  
            renameMe "Hello World " `shouldBe` "Hello World Hello World "