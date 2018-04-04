{-
   Excited without bugs, have fun ("▔□▔)/hi~♡ Nasy.
   -----------------------------------------------
   |
   |             *         *
   |                  .                .
   |           .
   |     *                      ,
   |                   .
   |
   |                               *
   |          |\___/|
   |          )    -(             .              '
   |         =\  -  /=
   |           )===(       *
   |          /   - \
   |          |-    |
   |         /   -   \     0.|.0
   |  NASY___\__( (__/_____(\=/)__+1s____________
   |  ______|____) )______|______|______|______|_
   |  ___|______( (____|______|______|______|____
   |  ______|____\_|______|______|______|______|_
   |  ___|______|______|______|______|______|____
   |  ______|______|______|______|______|______|_
   |  ___|______|______|______|______|______|____

   -----------------------------------------------

   Author              : Nasy https://nasy.moe <Nasy>
   Date                : Mar 10, 2018
   Email               : echo bmFzeXh4QGdtYWlsLmNvbQo= | base64 -D
   Filename            : Views.elm
   Last modified by    : Nasy
   Last modified time  : Mar 10, 2018
   License             : MIT

   -----------------------------------------------

   There are more things in heaven and earth, Horatio, than are dreamt.
      From "Hamlet"
-}


module Views exposing (..)

import Html exposing (..)
import Html.Attributes exposing (..)
import Html.Events exposing (..)
import Json.Encode exposing (string)
import Msgs exposing (Msg)
import Models exposing (BlogModel, BlogsModel, Model, Route(..))
import RemoteData exposing (WebData)


view : Model -> Html Msg
view model =
    div [ id "container" ]
        [ header [ id "header", class "header" ] <| header_view model
        , main_ [ id "main" ] <| main_view model
        , footer [ id "footer", class "footer", onClick Msgs.Up2Top ] footer_view
        ]



-- Header Views --


header_view : Model -> List (Html Msg)
header_view model =
    [ section
        [ class "header-section" ]
        [ h2
            [ class "header-section-title title" ]
            [ text "Nasy Land" ]
        , p
            [ class "header-section-description description" ]
            [ text "Nasy 栽花，养鱼，闲聊的地方～♡" ]
        ]
    , section [ class "header-section" ] <| nav_view "header"
    ]



-- Main Views --


main_view : Model -> List (Html Msg)
main_view model =
    case model.settings.route of
        Normal ->
            [ h2 [ class "main-h2" ] [ text "Main H2 Text" ]
            , p [ class "main-p" ] [ text "Main P text" ]
            , a [ href "blogs123" ] [ text "A clickable hyperlink" ]
            , blogs_view model.blogs
            ]

        BlogRoute ->
            [ h2 [ class "main-h2" ] [ text "Main H2 Text" ]
            , p [ class "main-p" ] [ text "Main P text" ]
            , a [ href "blogs123" ] [ text "A clickable hyperlink" ]
            , blog_view model.blog
            ]

        NotFoundRoute ->
            [ h2 [ class "main-h2" ] [ text "Main H2 Text Other" ], notfound ]



-- Footer Views --


footer_view : List (Html Msg)
footer_view =
    [ section
        [ class "footer-section" ]
        [ p [] [ text "Copyright © 2018 Nasy" ] ]
    , section [ class "footer-section" ] <| nav_view "footer"
    ]



-- Not Found--


notfound : Html Msg
notfound =
    p [ id "failure" ] [ text "404 Not Found" ]



-- Nav View --


nav_view : String -> List (Html Msg)
nav_view base =
    [ nav
        [ class "header-section-nav nav" ]
        [ ul []
            [ li
                [ class <| base ++ "-section-nav-list nav-list" ]
                [ a [ href "https://nasy.me", title "Who is Nasy?" ] [ text "Nasy" ] ]
            , li
                [ class <| base ++ "-section-nav-list nav-list" ]
                [ a [ href "/", title "Blog" ] [ text "Blog" ] ]
            , li
                [ class <| base ++ "-section-nav-list nav-list" ]
                [ a [ href "https://github.com/nasyxx", title "GitHub" ] [ text "GitHub" ] ]
            , li
                [ class <| base ++ "-section-nav-list nav-list" ]
                [ a [ href "https://twitter.com/nasyxx", title "Twitter" ] [ text "Twitter" ] ]
            , li
                [ class <| base ++ "-section-nav-list nav-list" ]
                [ a [ href "/more", title "More" ] [ text "More" ] ]
            ]
        ]
    ]



-- Blog View --


blog_view : WebData BlogModel -> Html Msg
blog_view res =
    case res of
        RemoteData.NotAsked ->
            div [] [ text "NotAsked" ]

        RemoteData.Loading ->
            p [ class "blog-loading" ] [ text "Loading Blog" ]

        RemoteData.Success blog ->
            section [ id "blog", class "blog" ] <| blog_ blog

        RemoteData.Failure err ->
            text <| toString err


blog_ : BlogModel -> List (Html Msg)
blog_ blog =
    [ header [ class "blog-header" ] [ tag_view blog ]
    , text_html "section" [ id "blog-content", class "blog-content" ] blog.content
    ]



-- Blogs View --


blogs_view : WebData BlogsModel -> Html Msg
blogs_view res =
    case res of
        RemoteData.NotAsked ->
            div [] [ text "NotAsked" ]

        RemoteData.Loading ->
            p [ class "blogs-list-loading" ] [ text "Loading Blogs List" ]

        RemoteData.Success blogs ->
            section [ id "blogs-list", class "blogs-list" ] <| blogs_list blogs

        RemoteData.Failure err ->
            text <| toString err


blogs_list_single : BlogModel -> List (Html Msg)
blogs_list_single blog =
    [ header [ class "blogs-list-header" ]
        [ a [ href ("/blog/" ++ blog.blog_path) ] [ h3 [] [ text blog.title ] ] ]
    , tag_view blog
    ]


blogs_list : BlogsModel -> List (Html Msg)
blogs_list blogs =
    List.map blogs_list_single blogs |> List.concat



-- Tag View --


tag_view : BlogModel -> Html Msg
tag_view blog =
    section [ class "tags", class "blogs-list-tags" ]
        [ section [ class "tags-author", class "fas fa-pencil-alt" ] [ span [] [ text blog.author ] ]
        , section [ class "tags-time" ] [ time [ datetime <| blog.datetime ] [] ]
        , section [ class "tags-summary" ] [ span [] [ text blog.summary ] ]
        , section [ class "tags-categories" ] [ tag_list "categories" blog.categories ]
        , section [ class "tags-tags" ] [ tag_list "tag" blog.tags ]
        ]


tag_li : String -> String -> Html Msg
tag_li prefix tag =
    li [ class "tags-list-li" ]
        [ a [ href <| "/" ++ prefix ++ "/" ++ tag, class "tags-list-li-a" ]
            [ text tag ]
        ]


tag_list : String -> List String -> Html Msg
tag_list prefix tags =
    ul [] <| List.map2 tag_li (List.repeat (List.length tags) prefix) tags



-- Utils --


text_html : String -> List (Attribute msg) -> String -> Html msg
text_html node_string attributes html_string =
    node node_string
        ((++)
            [ string html_string |> Html.Attributes.property "innerHTML" ]
            attributes
        )
        []
